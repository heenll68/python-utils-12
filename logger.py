import logging
import sys
from datetime import datetime

# Configure centralized application logging
def setup_logger(name: str = "autoclicker") -> logging.Logger:
    """Initializes a standard console logger for the project."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Output to stdout for easier integration with task runners
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Instantiate default logger for utility modules
logger = setup_logger()

def log_event(message: str, level: str = "info") -> None:
    """Helper for quick diagnostic message piping."""
    if level.lower() == "error":
        logger.error(message)
    elif level.lower() == "warning":
        logger.warning(message)
    else:
        logger.info(message)