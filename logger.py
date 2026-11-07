import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "autoclicker", log_file: str = "app.log") -> logging.Logger:
    """
    Configures a rotating file logger for the autoclicker application.
    Limits file size to 1MB and keeps 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotating file handler configuration
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1024 * 1024, backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        # Stream handler for console visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger