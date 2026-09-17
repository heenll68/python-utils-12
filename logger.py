import os
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_FILE = "autoclicker.log"
DEFAULT_MAX_BYTES = 1 * 1024 * 1024  # 1 MB log file limit
DEFAULT_BACKUP_COUNT = 3  # Keep up to 3 rotated log files
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def setup_logger(
    name: str = "autoclicker",
    log_file: str = DEFAULT_LOG_FILE,
    max_bytes: int = DEFAULT_MAX_BYTES,
    backup_count: int = DEFAULT_BACKUP_COUNT,
    level: int = logging.INFO
) -> logging.Logger:
    """Configures and returns a logger with rotating file and stream handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if initialized multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(LOG_FORMAT)

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating log file handler
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (PermissionError, OSError) as err:
        logger.warning(f"Failed to setup file logging: {err}")

    return logger
