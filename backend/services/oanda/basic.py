import logging
import os

import matplotlib

matplotlib.use('Agg')  # Use Agg backend for non-GUI plotting

import matplotlib.pyplot as plt
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from oanda_api import OandaAPI

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load configuration from environment variables or default values
INSTRUMENT = os.getenv('INSTRUMENT', 'EUR_USD')
GRANULARITY = os.getenv('GRANULARITY', 'H1')
COUNT = int(os.getenv('COUNT', 500))

# Initialize OandaAPI
oanda = OandaAPI()

# Directory to save plots
PLOTS_DIR = 'plots'
if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)

# Fetch historical data
def fetch_and_prepare_data(instrument, granularity, count):
    try:
        logging.info(f"Fetching historical data for {instrument} with granularity {granularity} and count {count}")    
        raw_data = oanda.get_historical_data(instrument, granularity, count)
        df = pd.DataFrame([{
            'time': candle['time'],
            'Open': float(candle['mid']['o']),
            'High': float(candle['mid']['h']),
            'Low': float(candle['mid']['l']),
            'Close': float(candle['mid']['c']),
            'Volume': candle['volume']
        } for candle in raw_data['candles']])
        
        logging.info(f"Raw data fetched: {df.head()}")        
        
        # Handle potential issues with datetime parsing
        df['time'] = pd.to_datetime(df['time'], errors='coerce')
        logging.info(f"Data after datetime parsing: {df.head()}")
        
        df = df.dropna(subset=['time'])
        df = df.set_index('time')
        logging.info(f"Data after dropping NA values and setting index: {df.head()}")            
        return df
    
    except Exception as e:
        logging.error(f"Error fetching and preparing data: {e}")
        raise

# Define strategy
class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        logging.info("Initializing SMA strategy")
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
        logging.info(f"SMA1: {self.sma1[:5]}")
        logging.info(f"SMA2: {self.sma2[:5]}")

    def next(self):
        logging.info("Running next step of SMA strategy")
        if crossover(self.sma1, self.sma2):
            self.buy()
            logging.info("Buy signal")
        elif crossover(self.sma2, self.sma1):
            self.sell()
            logging.info("Sell signal")

@app.route('/backtest', methods=['GET'])
def backtest():
    instrument = request.args.get('instrument', INSTRUMENT)
    granularity = request.args.get('granularity', GRANULARITY)
    count = int(request.args.get('count', COUNT))

    try:
        # Fetch and prepare data
        data = fetch_and_prepare_data(instrument, granularity, count)
        logging.info(f"Data ready for backtest: {data.head()}")

        # Run backtest
        bt = Backtest(data, SmaCross, cash=10000, commission=.002)
        logging.info("Backtest initialized")
        results = bt.run()
        logging.info("Backtest run completed")

        # Debugging equity curve
        equity_curve = results._equity_curve
        logging.info(f"Equity curve: {equity_curve.head()}")
        
        # Handle NaT values in DrawdownDuration column
        equity_curve['DrawdownDuration'] = equity_curve['DrawdownDuration'].apply(lambda x: x if pd.notnull(x) else None)
        logging.info(f"Equity curve after handling NaT values: {equity_curve.head()}")

        # # Convert the equity curve to JSON format
        # equity_curve_reset = equity_curve.reset_index()
        # logging.info(f"Equity curve after reset index: {equity_curve_reset.head()}")

        # equity_curve_json = equity_curve_reset.to_dict(orient='records')
        # logging.info(f"Equity curve JSON: {equity_curve_json[:5]}")
        
        # return jsonify(equity_curve_json)

        # Plotting the equity curve
        plt.figure(figsize=(10, 6))
        plt.plot(equity_curve.index, equity_curve['Equity'], label='Equity Curve')
        plt.title('Equity Curve')
        plt.xlabel('Time')
        plt.ylabel('Equity')
        plt.legend()
        plt.grid(True)
        plot_path = os.path.join(PLOTS_DIR, 'equity_curve.png')
        plt.savefig(plot_path)
        plt.close()
                
    except Exception as e:
        logging.error(f"Error in backtest: {e}")
        return jsonify({'error': str(e)}), 500
    
    # Route to serve plots
@app.route('/plots/<filename>')
def serve_plot(filename):
    return send_from_directory(PLOTS_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
