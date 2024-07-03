import os

# Trading parameters
TRADE_INSTRUMENTS = os.getenv("TRADE_INSTRUMENTS", ["EUR_USD", "GBP_USD", "USD_JPY"]).split(',')
TRADE_UNITS = int(os.getenv("TRADE_UNITS", 1000))
STOP_LOSS = int(os.getenv("STOP_LOSS", 20))  # in pips
TAKE_PROFIT = int(os.getenv("TAKE_PROFIT", 50))  # in pips
TRAILING_STOP_LOSS = int(os.getenv("TRAILING_STOP_LOSS", 10))  # in pips
TIMEFRAME = os.getenv("TIMEFRAME", "H1")  # 1-hour candles

# BackTesting Type control
BT_TYPE = os.getenv('BT_TYPE', 'Strategy')  # STRATEGY or SCENARIO

# State Machine Control
STATE_MACHINE = os.getenv('STATE_MACHINE', 'True').lower() == 'true'  # Set to False to disable state machine control

# Switches for Indicators
SWITCHES = {
    "RSI": os.getenv("RSI_SWITCH", 'False').lower() == 'true',
    "MACD": os.getenv("MACD_SWITCH", 'False').lower() == 'true',
    "SMA": os.getenv("SMA_SWITCH", 'True').lower() == 'true',
    "EMA": os.getenv("EMA_SWITCH", 'False').lower() == 'true',
    "BOLLINGER_BANDS": os.getenv("BOLLINGER_BANDS_SWITCH", 'False').lower() == 'true',
    "STOCHASTIC": os.getenv("STOCHASTIC_SWITCH", 'False').lower() == 'true'
}

# State Machine Adjustments to Risk Levels
GREEN = int(os.getenv("GREEN_RISK_LEVEL", 4))
YELLOW = int(os.getenv("YELLOW_RISK_LEVEL", 3))
RED = int(os.getenv("RED_RISK_LEVEL", 2))

# Execution parameters
MAX_CONCURRENT_TRADES = int(os.getenv("MAX_CONCURRENT_TRADES", 5))
SLEEP_INTERVAL = int(os.getenv("SLEEP_INTERVAL", 60))  # in seconds

# Additional Indicators
CONSTANTS = {
    'EMA_FAST': int(os.getenv('EMA_FAST', 12)),
    'EMA_SLOW': int(os.getenv('EMA_SLOW', 26)),
    'SMA_FAST': int(os.getenv('SMA_FAST', 50)),
    'SMA_SLOW': int(os.getenv('SMA_SLOW', 200)),
    'RSI_PERIOD': int(os.getenv('RSI_PERIOD', 14)),
    'MACD_SLOW': int(os.getenv('MACD_SLOW', 26)),
    'MACD_FAST': int(os.getenv('MACD_FAST', 12)),
    'MACD_SIGNAL': int(os.getenv('MACD_SIGNAL', 9)),
    'BB_PERIOD': int(os.getenv('BB_PERIOD', 20)),
    'BB_STD_DEV': int(os.getenv('BB_STD_DEV', 2)),
    'STOCHASTIC_PERIOD': int(os.getenv('STOCHASTIC_PERIOD', 14)),
    'STOCHASTIC_SMOOTH_K': int(os.getenv('STOCHASTIC_SMOOTH_K', 3)),
    'STOCHASTIC_SMOOTH_D': int(os.getenv('STOCHASTIC_SMOOTH_D', 3)),
    'GRANULARITY': os.getenv('GRANULARITY', 'D'),
    'CANDLES_COUNT': int(os.getenv('CANDLES_COUNT', 100))
}

# RSI Indicator
RSI_PERIOD = CONSTANTS['RSI_PERIOD']
RSI_OVERBOUGHT = int(os.getenv('RSI_OVERBOUGHT', 70))
RSI_OVERSOLD = int(os.getenv('RSI_OVERSOLD', 30))

# MACD Indicator
MACD_FAST_PERIOD = CONSTANTS['MACD_FAST']
MACD_SLOW_PERIOD = CONSTANTS['MACD_SLOW']
MACD_SIGNAL_PERIOD = CONSTANTS['MACD_SIGNAL']

# Simple Moving Average Indicator
SMA_PERIOD = CONSTANTS['SMA_FAST']
SMA_FAST = int(os.getenv('SMA_FAST', 10))
SMA_SLOW = int(os.getenv('SMA_SLOW', 50))

# Exponential Moving Average Indicator
EMA_PERIOD = CONSTANTS['EMA_FAST']
EMA_FAST = int(os.getenv('EMA_FAST', 10))
EMA_SLOW = int(os.getenv('EMA_SLOW', 50))

# Bollinger Bands Indicator
BOLLINGER_BANDS_PERIOD = CONSTANTS['BB_PERIOD']
BOLLINGER_BANDS_STD_DEV = CONSTANTS['BB_STD_DEV']

# Stochastic Oscillator Indicator
STOCHASTIC_K_PERIOD = CONSTANTS['STOCHASTIC_PERIOD']
STOCHASTIC_D_PERIOD = CONSTANTS['STOCHASTIC_SMOOTH_D']

# Consolidated Indicator Settings
INDICATORS = {
    "RSI": {
        "enabled": SWITCHES["RSI"],
        "period": RSI_PERIOD,
        "overbought": RSI_OVERBOUGHT,
        "oversold": RSI_OVERSOLD
    },
    "MACD": {
        "enabled": SWITCHES["MACD"],
        "fast_period": MACD_FAST_PERIOD,
        "slow_period": MACD_SLOW_PERIOD,
        "signal_period": MACD_SIGNAL_PERIOD
    },
    "SMA": {
        "enabled": SWITCHES["SMA"],
        "period": SMA_PERIOD,
        "fast": SMA_FAST,
        "slow": SMA_SLOW
    },
    "EMA": {
        "enabled": SWITCHES["EMA"],
        "period": EMA_PERIOD,
        "fast": EMA_FAST,
        "slow": EMA_SLOW
    },
    "BOLLINGER_BANDS": {
        "enabled": SWITCHES["BOLLINGER_BANDS"],
        "period": BOLLINGER_BANDS_PERIOD,
        "std_dev": BOLLINGER_BANDS_STD_DEV
    },
    "STOCHASTIC": {
        "enabled": SWITCHES["STOCHASTIC"],
        "k_period": STOCHASTIC_K_PERIOD,
        "d_period": STOCHASTIC_D_PERIOD
    }
}

# Scenarios for state machine logic
SCENARIOS = {
    "LONG": {
        "RSI_PERIOD": RSI_PERIOD,
        "RSI_OVERBOUGHT": RSI_OVERBOUGHT,
        "RSI_OVERSOLD": RSI_OVERSOLD,
        "MACD_FAST_PERIOD": MACD_FAST_PERIOD,
        "MACD_SLOW_PERIOD": MACD_SLOW_PERIOD,
        "MACD_SIGNAL_PERIOD": MACD_SIGNAL_PERIOD,
        "SMA_PERIOD": SMA_PERIOD,
        "SMA_FAST": SMA_FAST,
        "SMA_SLOW": SMA_SLOW,
        "EMA_PERIOD": EMA_PERIOD,
        "EMA_FAST": EMA_FAST,
        "EMA_SLOW": EMA_SLOW,
        "BOLLINGER_BANDS_PERIOD": BOLLINGER_BANDS_PERIOD,
        "BOLLINGER_BANDS_STD_DEV": BOLLINGER_BANDS_STD_DEV,
        "STOCHASTIC_K_PERIOD": STOCHASTIC_K_PERIOD,
        "STOCHASTIC_D_PERIOD": STOCHASTIC_D_PERIOD,
        "INDICATORS": {
            "RSI": True,
            "MACD": True,
            "SMA": True,
            "EMA": True,
            "BOLLINGER_BANDS": True,
            "STOCHASTIC": True
        }
    },
    "SHORT": {
        "RSI_PERIOD": 10,
        "RSI_OVERBOUGHT": 75,
        "RSI_OVERSOLD": 25,
        "MACD_FAST_PERIOD": 15,
        "MACD_SLOW_PERIOD": 30,
        "MACD_SIGNAL_PERIOD": 10,
        "SMA_PERIOD": 200,
        "SMA_FAST": 30,
        "SMA_SLOW": 100,
        "EMA_PERIOD": 200,
        "EMA_FAST": 30,
        "EMA_SLOW": 100,
        "BOLLINGER_BANDS_PERIOD": 20,
        "BOLLINGER_BANDS_STD_DEV": 2,
        "STOCHASTIC_K_PERIOD": 14,
        "STOCHASTIC_D_PERIOD": 3,
        "INDICATORS": {
            "RSI": True,
            "MACD": True,
            "SMA": True,
            "EMA": True,
            "BOLLINGER_BANDS": True,
            "STOCHASTIC": True
        }
    }
}

# Optimization ranges for different strategies
OPTIMIZATION_RANGES = {
    "RSI": {
        "RSI_PERIOD": [10, 20, 30],
        "RSI_OVERBOUGHT": [50, 60, 70],
        "RSI_OVERSOLD": [30, 40, 50]
    },
    "MACD": {
        "MACD_FAST_PERIOD": [5, 10, 15],
        "MACD_SLOW_PERIOD": [20, 25, 30],
        "MACD_SIGNAL_PERIOD": [5, 10, 15]
    },
    "SMA": {
        "SMA_PERIOD": [50, 100, 200],
        "SMA_FAST": [10, 20, 30],
        "SMA_SLOW": [50, 100, 200]
    },
    "EMA": {
        "EMA_PERIOD": [50, 100, 200],
        "EMA_FAST": [10, 20, 30],
        "EMA_SLOW": [50, 100, 200]
    },
    "BOLLINGER_BANDS": {
        "BOLLINGER_BANDS_PERIOD": [10, 20, 30],
        "BOLLINGER_BANDS_STD_DEV": [1, 2, 3]
    },
    "STOCHASTIC": {
        "STOCHASTIC_K_PERIOD": [10, 14, 18],
        "STOCHASTIC_D_PERIOD": [3, 5, 7]
    }
}
