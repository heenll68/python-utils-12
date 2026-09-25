import logging
import os
import sys
from datetime import datetime


def setup_logger(log_to_file: bool = True, log_level: int = logging.INFO) -> logging.Logger:
    """Configures and returns the application logger for the autoclicker."""
    logger = logging.getLogger("autoclicker")
    logger.setLevel(log_level)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    if log_to_file:
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(
            log_dir, f"autoclicker_{datetime.now().strftime('%Y%m%d')}.log"
        )
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_click_event(logger: logging.Logger, x: int, y: int, button: str) -> None:
    """Helper utility for standardizing click event logs."""
    logger.debug(f"Action triggered: {button} click at coordinates ({x}, {y})")


# Default global logger instance
click_logger = setup_logger()
