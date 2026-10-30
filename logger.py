import logging
import sys
from typing import Optional

def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """Configures a standardized logger with robust error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler with error recovery
    if log_file:
        try:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (IOError, PermissionError) as e:
            logger.error(f"Failed to initialize log file {log_file}: {e}")
            # Fallback to stdout only if file access fails
            
    return logger

def log_execution_error(logger: logging.Logger, error: Exception) -> None:
    """Logs specific autoclicker operational exceptions for debugging."""
    if isinstance(error, KeyboardInterrupt):
        logger.info("Autoclicker execution stopped by user.")
    elif isinstance(error, RuntimeError):
        logger.error(f"Runtime critical error: {error}")
    else:
        logger.exception(f"Unexpected error encountered: {type(error).__name__}")