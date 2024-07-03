import logging
import os

# Ensure the logging directory exists
log_directory = os.getenv('LOG_DIRECTORY', 'All-Logs')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
log_file = os.getenv('LOG_FILE', 'forex_trading_robot.log')
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

logging.basicConfig(
    filename=os.path.join(log_directory, log_file),
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_event(message, level='info'):
    level = level.lower()
    if level == 'debug':
        logging.debug(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.info(message)
