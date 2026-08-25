import logging
import sys
from pathlib import Path

# Configure logger for autoclicker with robust error handling
def setup_logger(log_file: str = "autoclicker.log", level: int = logging.INFO) -> logging.Logger:
    """Initialize logger with file and console handlers, handling setup errors."""
    logger = logging.getLogger("autoclicker")
    logger.setLevel(level)
    if logger.handlers:
        logger.handlers.clear()
    try:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(file_format)
        logger.addHandler(console_handler)
    except PermissionError as e:
        # Handle permission denied for log file
        print(f"Permission error creating log file: {e}")
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)
    except Exception as e:
        # Catch all other setup errors
        print(f"Unexpected error setting up logger: {e}")
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING)
        logger.addHandler(console_handler)
    return logger

def log_with_error_handling(logger: logging.Logger, message: str, level: str = "info"):
    """Log message safely, handling edge cases like empty message or invalid level."""
    if not isinstance(message, str) or not message.strip():
        # Edge case: invalid message
        logger.warning("Invalid log message provided: must be non-empty string")
        return
    valid_levels = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "critical": logger.critical
    }
    log_func = valid_levels.get(level.lower())
    if log_func is None:
        # Edge case: invalid level
        logger.error(f"Invalid log level '{level}'. Defaulting to info.")
        log_func = logger.info
    try:
        log_func(message)
    except Exception as e:
        # Fallback if logging itself fails
        print(f"Failed to log message: {message}. Error: {e}")

if __name__ == "__main__":
    logger = setup_logger()
    log_with_error_handling(logger, "Autoclicker started", "info")
    log_with_error_handling(logger, "", "info")
    log_with_error_handling(logger, "Test message", "invalid_level")
    log_with_error_handling(logger, 123, "info")
