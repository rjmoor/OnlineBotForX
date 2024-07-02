# Trading parameters
TRADE_INSTRUMENTS = ["EUR_USD", "GBP_USD", "USD_JPY"]
TRADE_UNITS = 1000
STOP_LOSS = 20  # in pips
TAKE_PROFIT = 50  # in pips
TRAILING_STOP_LOSS = 10  # in pips
TIMEFRAME = "H1"  # 1-hour candles

# BackTesting Type control
BT_TYPE = 'Strategy'  # STRATEGY or SCENARIO

# State Machine Control
STATE_MACHINE = True  # Set to False to disable state machine control

# Switches for Indicators
SWITCHES = {
    "RSI": False,
    "MACD": False,
    "SMA": True,
    "EMA": False,
    "BOLLINGER_BANDS": False,
    "STOCHASTIC": False
}

# State Machine Adjustments to Risk Levels
GREEN = 4
YELLOW = 3
RED = 2

# Execution parameters
MAX_CONCURRENT_TRADES = 5
SLEEP_INTERVAL = 60  # in seconds

### Additional Indicators ###

CONSTANTS = {
    'EMA_FAST': 12,
    'EMA_SLOW': 26,
    'SMA_FAST': 50,
    'SMA_SLOW': 200,
    'RSI_PERIOD': 14,
    'MACD_SLOW': 26,
    'MACD_FAST': 12,
    'MACD_SIGNAL': 9,
    'BB_PERIOD': 20,
    'BB_STD_DEV': 2,
    'STOCHASTIC_PERIOD': 14,
    'STOCHASTIC_SMOOTH_K': 3,
    'STOCHASTIC_SMOOTH_D': 3,
    'GRANULARITY': 'D',  # 'M', 'H1', etc.
    'CANDLES_COUNT': 100
}


# RSI Indicator
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

# MACD Indicator
MACD_FAST_PERIOD = 12
MACD_SLOW_PERIOD = 26
MACD_SIGNAL_PERIOD = 9

# Simple Moving Average Indicator
SMA_PERIOD = 50
SMA_FAST = 10
SMA_SLOW = 50

# Exponential Moving Average Indicator
EMA_PERIOD = 50
EMA_FAST = 10
EMA_SLOW = 50

# Bollinger Bands Indicator
BOLLINGER_BANDS_PERIOD = 20
BOLLINGER_BANDS_STD_DEV = 2

# Stochastic Oscillator Indicator
STOCHASTIC_K_PERIOD = 14
STOCHASTIC_D_PERIOD = 3

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

# Scenario parameters for different risk levels
SCENARIOS = {
    "LONG": {
        "RSI_PERIOD": 14,
        "RSI_OVERBOUGHT": 70,
        "RSI_OVERSOLD": 30,
        "MACD_FAST_PERIOD": 12,
        "MACD_SLOW_PERIOD": 26,
        "MACD_SIGNAL_PERIOD": 9,
        "SMA_PERIOD": 50,
        "SMA_FAST": 10,
        "SMA_SLOW": 50,
        "EMA_PERIOD": 50,
        "EMA_FAST": 10,
        "EMA_SLOW": 50,
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
    },
    "VOLATILE": {
        "RSI_PERIOD": 20,
        "RSI_OVERBOUGHT": 65,
        "RSI_OVERSOLD": 35,
        "MACD_FAST_PERIOD": 10,
        "MACD_SLOW_PERIOD": 22,
        "MACD_SIGNAL_PERIOD": 8,
        "SMA_PERIOD": 100,
        "SMA_FAST": 20,
        "SMA_SLOW": 100,
        "EMA_PERIOD": 100,
        "EMA_FAST": 20,
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
