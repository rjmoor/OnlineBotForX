# trade_machine.py
import pandas as pd
import matplotlib.pyplot as plt
from oanda_api import OandaAPI
from fundamental import TradingIndicators
from variables import TRADE_INSTRUMENTS, STATE_MACHINE, SWITCHES, SCENARIOS, BT_TYPE, SMA_PERIOD, EMA_PERIOD, OPTIMIZATION_RANGES
import logging

class TradeMachine:
    def __init__(self, oanda_api):
        self.oanda_api = oanda_api
        self.state_machine_enabled = STATE_MACHINE
        self.backtesting_enabled = BT_TYPE == 'Strategy'
        self.indicator_switches = SWITCHES
        self.initialize_states()

    def initialize_states(self):
        self.states = {pair: 'red' for pair in TRADE_INSTRUMENTS}

    def update_state(self, instrument, new_state):
        self.states[instrument] = new_state

    def fetch_data(self, instrument, granularity="H1", count=1000):
        try:
            data = self.oanda_api.load_historical_data(instrument, granularity, count)
            if not data:
                data = self.oanda_api.get_historical_data(instrument, granularity, count)
                self.oanda_api.save_historical_data(instrument, data, granularity, count)
            return pd.DataFrame(data['candles'])
        except Exception as e:
            logging.error(f"Error fetching data for {instrument}: {e}")
            raise

    def process_data(self, df):
        try:
            df['time'] = pd.to_datetime(df['time'])
            for col in ['c', 'h', 'l', 'o']:
                df[col] = df['mid'][col].astype(float)
            df.rename(columns={'c': 'close', 'h': 'high', 'l': 'low', 'o': 'open'}, inplace=True)
            return df
        except Exception as e:
            logging.error(f"Error processing data: {e}")
            raise

    def analyze_pair(self, instrument):
        try:
            df = self.process_data(self.fetch_data(instrument))
            indicators = TradingIndicators(df)
            scenario = SCENARIOS['LONG'] if self.states[instrument] == 'green' else SCENARIOS['SHORT']
            for ind, settings in scenario['INDICATORS'].items():
                if settings:
                    self.apply_indicator(ind, indicators, scenario)
            self.plot_indicators(df, indicators, instrument)
        except Exception as e:
            logging.error(f"Error analyzing pair {instrument}: {e}")

    def apply_indicator(self, ind, indicators, scenario):
        # Scenario-based logic for dynamic switches
        scenario = SCENARIOS['LONG'] if self.states[instrument] == 'green' else SCENARIOS['SHORT']
        for ind, settings in scenario['INDICATORS'].items():
            if settings:
                if ind == "RSI" and self.indicator_switches[ind]:
                    indicators.calculate_rsi(period=scenario['RSI_PERIOD'])
                elif ind == "MACD" and self.indicator_switches[ind]:
                    indicators.calculate_macd(slow=scenario['MACD_SLOW_PERIOD'], fast=scenario['MACD_FAST_PERIOD'], signal=scenario['MACD_SIGNAL_PERIOD'])
                elif ind == "SMA" and self.indicator_switches[ind]:
                    indicators.calculate_sma(period=scenario['SMA_PERIOD'])
                elif ind == "EMA" and self.indicator_switches[ind]:
                    indicators.calculate_ema(period=scenario['EMA_PERIOD'])
                elif ind == "BOLLINGER_BANDS" and self.indicator_switches[ind]:
                    indicators.calculate_bollinger_bands(period=scenario['BOLLINGER_BANDS_PERIOD'], std_dev=scenario['BOLLINGER_BANDS_STD_DEV'])
                elif ind == "STOCHASTIC" and self.indicator_switches[ind]:
                    indicators.calculate_stochastic(period=scenario['STOCHASTIC_K_PERIOD'], smooth_k=scenario['STOCHASTIC_K_PERIOD'], smooth_d=scenario['STOCHASTIC_D_PERIOD'])

        # Example conditions for state transitions based on combined indicator analysis
        rsi = indicators.calculate_rsi()
        macd = indicators.calculate_macd()
        bollinger_bands = indicators.calculate_bollinger_bands()

        if rsi.iloc[-1] < 30:
            self.update_state(instrument, 'green')
        elif 30 <= rsi.iloc[-1] <= 70:
            self.update_state(instrument, 'yellow')
        else:
            self.update_state(instrument, 'red')

    def run(self):
        self.initialize_states()
        for pair in self.states:
            self.analyze_pair(pair)
            print(f"{pair} state: {self.states[pair]}")

        if self.backtesting_enabled:
            self.run_backtest()

        if self.state_machine_enabled and self.backtesting_enabled:
            self.optimize()

    def run_backtest(self):
        print("Running backtest...")
        for pair in self.states:
            data = self.fetch_data(pair)
            df = self.process_data(data)
            indicators = TradingIndicators(df)

            if self.indicator_switches["RSI"]:
                indicators.calculate_rsi()
            if self.indicator_switches["MACD"]:
                indicators.calculate_macd()
            if self.indicator_switches["SMA"]:
                indicators.calculate_sma(period=SMA_PERIOD)
            if self.indicator_switches["EMA"]:
                indicators.calculate_ema(period=EMA_PERIOD)
            if self.indicator_switches["BOLLINGER_BANDS"]:
                indicators.calculate_bollinger_bands()

            self.plot_indicators(df, indicators, pair)

    def plot_indicators(self, df, indicators, instrument):
        fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))
        df['close'].plot(ax=axes[0])
        axes[0].set_title(f'{instrument} Price')

        if self.indicator_switches["RSI"]:
            indicators.calculate_rsi().plot(ax=axes[1])
            axes[1].set_title('RSI')

        if self.indicator_switches["MACD"]:
            macd = indicators.calculate_macd()
            macd.plot(ax=axes[2])
            axes[2].set_title('MACD')

        plt.tight_layout()
        plt.show()

    def optimize(self):
        logging.info('Starting optimization...')
        print("Optimizing...")
        for pair in self.states:
            data = self.fetch_data(pair)
            df = self.process_data(data)
            self.optimize_indicators(df, pair)
        logging.info('Optimization completed.')

    def optimize_indicators(self, df, instrument):
        for indicator, params in OPTIMIZATION_RANGES.items():
            if indicator == 'RSI':
                for period in params['RSI_PERIOD']:
                    df[f'RSI_{period}'] = TradingIndicators(df).calculate_rsi(period=period)
                    # Add your optimization logic here
            elif indicator == 'MACD':
                for fast in params['MACD_FAST_PERIOD']:
                    for slow in params['MACD_SLOW_PERIOD']:
                        for signal in params['MACD_SIGNAL_PERIOD']:
                            df['MACD'] = TradingIndicators(df).calculate_macd(fast=fast, slow=slow, signal=signal)
                            # Add your optimization logic here
            # Continue for other indicators...

# Example usage
if __name__ == "__main__":
    oanda = OandaAPI()
    trade_machine = TradeMachine(oanda)
    trade_machine.run()
    trade_machine.optimize()
