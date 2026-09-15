import logging
import os
import sys

def setup_logger(name: str = 'autoclicker', log_file: str = 'app.log') -> logging.Logger:
    """Configures a robust logger with file rotation and edge case handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Ensure directory existence
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError as e:
            print(f"Critical error: Could not create log directory: {e}", file=sys.stderr)
            return logger

    # File handler with error resilience
    try:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (PermissionError, IOError) as e:
        print(f"Warning: Logger file handler failed: {e}", file=sys.stderr)

    # Console output for immediate feedback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    return logger