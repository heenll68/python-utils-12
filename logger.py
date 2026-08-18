import logging

# Configure logger settings
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def log_click_event(click_data):
    """Logs click event data to the console and file."""
    if not isinstance(click_data, dict):
        logger.error('Invalid click data format, must be a dictionary')
        return
    
    try:
        logger.info('Click event: %s', click_data)
        with open('click_events.log', 'a') as log_file:
            log_file.write(f'{click_data}\n')
    except Exception as e:
        logger.error('Failed to log click event: %s', e)

def log_error(message):
    """Logs error messages to the console."""
    logger.error(message)

def log_info(message):
    """Logs informational messages to the console."""
    logger.info(message)
