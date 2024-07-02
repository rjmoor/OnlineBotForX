from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
from oanda_api import OandaAPI

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize OandaAPI
oanda = OandaAPI()

# Fetch historical data
def fetch_and_prepare_data(instrument, granularity, count):
    raw_data = oanda.get_historical_data(instrument, granularity, count)
    df = pd.DataFrame([{
        'time': candle['time'],
        'Open': float(candle['mid']['o']),
        'High': float(candle['mid']['h']),
        'Low': float(candle['mid']['l']),
        'Close': float(candle['mid']['c']),
        'Volume': candle['volume']
    } for candle in raw_data['candles']])
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    return df

# Define strategy
class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

@app.route('/backtest', methods=['GET'])
def backtest():
    instrument = 'EUR_USD'
    granularity = 'H1'
    count = 500

    # Fetch and prepare data
    data = fetch_and_prepare_data(instrument, granularity, count)

    # Run backtest
    bt = Backtest(data, SmaCross, cash=10000, commission=.002)
    results = bt.run()

    # Convert the equity curve to JSON format
    equity_curve = results._equity_curve.reset_index().to_dict(orient='records')

    return jsonify(equity_curve)

if __name__ == '__main__':
    app.run(debug=True)
