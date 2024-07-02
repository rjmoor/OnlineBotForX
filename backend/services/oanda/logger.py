import logging
import os

# Ensure the logging directory exists
if not os.path.exists('All-Logs'):
    os.makedirs('All-Logs')

# Configure logging
logging.basicConfig(
    filename='All-Logs/forex_trading_robot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_event(message):
    logging.info(message)
