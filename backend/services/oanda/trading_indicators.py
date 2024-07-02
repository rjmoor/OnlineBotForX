import pandas as pd
from variables import CONSTANTS

class TradingIndicators:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def calculate_rsi(self, period=CONSTANTS['RSI_PERIOD']):
        delta = self.data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        return self.data['RSI']

    def calculate_macd(self, slow=CONSTANTS['MACD_SLOW'], fast=CONSTANTS['MACD_FAST'], signal=CONSTANTS['MACD_SIGNAL']):
        self.data['EMA_fast'] = self.data['close'].ewm(span=fast, adjust=False).mean()
        self.data['EMA_slow'] = self.data['close'].ewm(span=slow, adjust=False).mean()
        self.data['MACD'] = self.data['EMA_fast'] - self.data['EMA_slow']
        self.data['MACD_signal'] = self.data['MACD'].ewm(span=signal, adjust=False).mean()
        self.data['MACD_hist'] = self.data['MACD'] - self.data['MACD_signal']
        return self.data[['MACD', 'MACD_signal', 'MACD_hist']]

    def calculate_bollinger_bands(self, period=CONSTANTS['BB_PERIOD'], std_dev=CONSTANTS['BB_STD_DEV']):
        self.data['SMA'] = self.data['close'].rolling(window=period).mean()
        self.data['BB_upper'] = self.data['SMA'] + (self.data['close'].rolling(window=period).std() * std_dev)
        self.data['BB_lower'] = self.data['SMA'] - (self.data['close'].rolling(window=period).std() * std_dev)
        return self.data[['BB_upper', 'BB_lower', 'SMA']]

    def calculate_stochastic(self, period=CONSTANTS['STOCHASTIC_PERIOD'], smooth_k=CONSTANTS['STOCHASTIC_SMOOTH_K'], smooth_d=CONSTANTS['STOCHASTIC_SMOOTH_D']):
        self.data['L14'] = self.data['low'].rolling(window=period).min()
        self.data['H14'] = self.data['high'].rolling(window=period).max()
        self.data['%K'] = 100 * ((self.data['close'] - self.data['L14']) / (self.data['H14'] - self.data['L14']))
        self.data['%D'] = self.data['%K'].rolling(window=smooth_d).mean()
        self.data['%K'] = self.data['%K'].rolling(window=smooth_k).mean()
        return self.data[['%K', '%D']]

    def calculate_ema(self, period):
        self.data[f'EMA_{period}'] = self.data['close'].ewm(span=period, adjust=False).mean()
        return self.data[f'EMA_{period}']

    def calculate_sma(self, period):
        self.data[f'SMA_{period}'] = self.data['close'].rolling(window=period).mean()
        return self.data[f'SMA_{period}']

    def calculate_ema_fast(self):
        return self.calculate_ema(CONSTANTS['EMA_FAST'])

    def calculate_ema_slow(self):
        return self.calculate_ema(CONSTANTS['EMA_SLOW'])

    def calculate_sma_fast(self):
        return self.calculate_sma(CONSTANTS['SMA_FAST'])

    def calculate_sma_slow(self):
        return self.calculate_sma(CONSTANTS['SMA_SLOW'])
