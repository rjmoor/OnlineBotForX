import time
from datetime import datetime
import pandas as pd
import variables
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.volatility import BollingerBands
from ta.momentum import StochasticOscillator
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from logger import log_event
from oanda_api import OandaAPI

class RSIStrategy(Strategy):
    RSI_PERIOD = 14
    RSI_OVERSOLD = 30
    RSI_OVERBOUGHT = 70

    def init(self):
        self.rsi = self.I(RSIIndicator, pd.Series(self.data.Close), self.RSI_PERIOD)

    def next(self):
        if self.rsi.rsi[-1] < self.RSI_OVERSOLD:
            self.buy()
        elif self.rsi.rsi[-1] > self.RSI_OVERBOUGHT:
            self.sell()

class SMACrossoverStrategy(Strategy):
    SMA_FAST = 10
    SMA_SLOW = 30

    def init(self):
        self.sma1 = self.I(SMAIndicator, pd.Series(self.data.Close), self.SMA_FAST)
        self.sma2 = self.I(SMAIndicator, pd.Series(self.data.Close), self.SMA_SLOW)

    def next(self):
        if crossover(self.sma1.sma_indicator(), self.sma2.sma_indicator()):
            self.buy()
        elif crossover(self.sma2.sma_indicator(), self.sma1.sma_indicator()):
            self.sell()

class EMACrossoverStrategy(Strategy):
    EMA_FAST = 12
    EMA_SLOW = 26

    def init(self):
        self.ema1 = self.I(EMAIndicator, pd.Series(self.data.Close), self.EMA_FAST)
        self.ema2 = self.I(EMAIndicator, pd.Series(self.data.Close), self.EMA_SLOW)

    def next(self):
        if crossover(self.ema1.ema_indicator(), self.ema2.ema_indicator()):
            self.buy()
        elif crossover(self.ema2.ema_indicator(), self.ema1.ema_indicator()):
            self.sell()

class MACDStrategy(Strategy):
    FAST = 12
    SLOW = 26
    SIGNAL = 9

    def init(self):
        self.macd = self.I(MACD, pd.Series(self.data.Close), self.FAST, self.SLOW, self.SIGNAL)

    def next(self):
        if crossover(self.macd.macd_diff(), self.macd.macd_signal()):
            self.buy()
        elif crossover(self.macd.macd_signal(), self.macd.macd_diff()):
            self.sell()

class BollingerBandsStrategy(Strategy):
    PERIOD = 20
    STDDEV = 2

    def init(self):
        self.bb = self.I(BollingerBands, pd.Series(self.data.Close), self.PERIOD, self.STDDEV)

    def next(self):
        if crossover(self.data.Close, self.bb.bollinger_lband()):
            self.buy()
        elif crossover(self.data.Close, self.bb.bollinger_hband()):
            self.sell()

class StochasticStrategy(Strategy):
    K_PERIOD = 14
    D_PERIOD = 3
    OVERSOLD = 20
    OVERBOUGHT = 80

    def init(self):
        self.stoch = self.I(StochasticOscillator, pd.Series(self.data.High), pd.Series(self.data.Low), pd.Series(self.data.Close), self.K_PERIOD, self.D_PERIOD)

    def next(self):
        if self.stoch.stoch_k()[-1] < self.OVERSOLD and crossover(self.stoch.stoch_k(), self.stoch.stoch_d()):
            self.buy()
        elif self.stoch.stoch_k()[-1] > self.OVERBOUGHT and crossover(self.stoch.stoch_d(), self.stoch.stoch_k()):
            self.sell()

def run_backtests(data):
    bt_data = data[['mid_o', 'mid_h', 'mid_l', 'mid_c']].rename(columns={'mid_o': 'Open', 'mid_h': 'High', 'mid_l': 'Low', 'mid_c': 'Close'})

    # SMA Strategy Backtest
    sma_bt = Backtest(bt_data, SMACrossoverStrategy, cash=10000, commission=0.002, exclusive_orders=True)
    sma_stats = sma_bt.run()
    print(f"SMA Strategy Performance:\n{sma_stats}")

    # RSI Strategy Backtest
    rsi_bt = Backtest(bt_data, RSIStrategy, cash=10000, commission=0.002, exclusive_orders=True)
    rsi_stats = rsi_bt.run()
    print(f"RSI Strategy Performance:\n{rsi_stats}")

    # MACD Strategy Backtest
    macd_bt = Backtest(bt_data, MACDStrategy, cash=10000, commission=0.002, exclusive_orders=True)
    macd_stats = macd_bt.run()
    print(f"MACD Strategy Performance:\n{macd_stats}")

    # EMA Strategy Backtest
    ema_bt = Backtest(bt_data, EMACrossoverStrategy, cash=10000, commission=0.002, exclusive_orders=True)
    ema_stats = ema_bt.run()
    print(f"EMA Strategy Performance:\n{ema_stats}")

    # Bollinger Bands Strategy Backtest
    bb_bt = Backtest(bt_data, BollingerBandsStrategy, cash=10000, commission=0.002, exclusive_orders=True)
    bb_stats = bb_bt.run()
    print(f"Bollinger Bands Strategy Performance:\n{bb_stats}")

    # Stochastic Strategy Backtest
    stoch_bt = Backtest(bt_data, StochasticStrategy, cash=10000, commission=0.002, exclusive_orders=True)
    stoch_stats = stoch_bt.run()
    print(f"Stochastic Strategy Performance:\n{stoch_stats}")

def main():
    api = OandaAPI()
    
    while True:
        for instrument in variables.TRADE_INSTRUMENTS:
            res, data = api.fetch_candles(instrument, count=100, granularity=variables.TIMEFRAME, as_df=True)
            if res == 200:
                run_backtests(data)
            else:
                print(f"Failed to fetch data for {instrument}")
                log_event(f"Failed to fetch data for {instrument}")

        time.sleep(variables.SLEEP_INTERVAL)

if __name__ == "__main__":
    main()
