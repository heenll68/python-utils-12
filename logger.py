import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance for the autoclicker.

    Args:
        name: The name of the logger module.
        level: The logging severity level.

    Returns:
        A configured logging.Logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    formatter: logging.Formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def log_event(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Helper to log application events with specific levels.

    Args:
        logger: The logger instance to use.
        message: The message string to record.
        level: The severity level string.
    """
    levels: dict = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error
    }
    
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)