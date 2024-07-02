import pandas as pd
from oanda.fundamental import TradingIndicators
from oanda.oanda_api import OandaAPI

class TradingStateMachine:
    def __init__(self, oanda_api):
        self.oanda_api = oanda_api
        self.states = {}

    def initialize_states(self):
        for pair in self.oanda_api.get_all_forex_pairs():
            self.states[pair] = 'red'  # Initialize all pairs to 'red'

    def update_state(self, instrument, new_state):
        self.states[instrument] = new_state

    def analyze_pair(self, instrument):
        data = self.oanda_api.load_historical_data(instrument)
        if not data:
            data = self.oanda_api.get_historical_data(instrument)
            self.oanda_api.save_historical_data(instrument, data)

        df = pd.DataFrame(data['candles'])
        df['time'] = pd.to_datetime(df['time'])
        df['close'] = df['mid']['c'].astype(float)
        df['high'] = df['mid']['h'].astype(float)
        df['low'] = df['mid']['l'].astype(float)
        df['open'] = df['mid']['o'].astype(float)

        indicators = TradingIndicators(df)
        rsi = indicators.calculate_rsi()
        macd = indicators.calculate_macd()

        # Example conditions for state transitions
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

# Example usage
if __name__ == "__main__":
    oanda = OandaAPI()
    trading_state_machine = TradingStateMachine(oanda)
    trading_state_machine.run()
