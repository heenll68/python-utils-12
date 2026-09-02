import logging
from typing import Any, Dict, Optional

class AutoClickerLogger:
    """Custom logger for autoclicker utilities.
    Handles logging of clicks, actions and errors with proper formatting.
    """
    def __init__(self, name: str = "autoclicker", level: str = "INFO", log_to_file: bool = False, filename: Optional[str] = None) -> None:
        """Initialize logger instance.
        Configures logging level and handler based on parameters.
        Args:
            name: Logger name.
            level: Logging level.
            log_to_file: Flag to enable file logging.
            filename: Log file path.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper(), logging.INFO))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger.handlers.clear()
        if log_to_file and filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_click(self, x: int, y: int, button: str = "left") -> None:
        """Log a click at given coordinates.
        Args:
            x: X position.
            y: Y position.
            button: Click button type.
        """
        msg = f"Click at ({x}, {y}) with {button} button"
        self.logger.info(msg)

    def log_action(self, action: str, details: Optional[Dict[str, Any]] = None) -> None:
        """Log an autoclicker action.
        Args:
            action: Action name.
            details: Optional details dict.
        """
        if details is None:
            details = {}
        msg = f"Action: {action}"
        if details:
            msg += f" Details: {details}"
        self.logger.info(msg)

    def log_error(self, error: str, exc: Optional[Exception] = None) -> None:
        """Log error details.
        Args:
            error: Error description.
            exc: Optional exception.
        """
        if exc:
            self.logger.error(f"{error}: {exc}")
        else:
            self.logger.error(error)

    def log_warning(self, warning: str) -> None:
        """Log a warning.
        Args:
            warning: Warning message.
        """
        self.logger.warning(warning)

if __name__ == "__main__":
    logger_instance = AutoClickerLogger(level="INFO")
    logger_instance.log_click(100, 200)
    logger_instance.log_action("test_action", {"speed": "fast"})
    logger_instance.log_warning("This is a test warning")
    logger_instance.log_error("This is a test error")
