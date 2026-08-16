import logging
from logging.handlers import RotatingFileHandler

# Configure logging settings
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'app.log'
LOG_SIZE = 5 * 1024 * 1024  # 5 MB
LOG_BACKUP_COUNT = 3

# Set up logger
logger = logging.getLogger('AutoClickerLogger')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_SIZE, backupCount=LOG_BACKUP_COUNT)
handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Add the handler to the logger
logger.addHandler(handler)

# Example function to log messages
def log_example():
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

if __name__ == '__main__':
    log_example()