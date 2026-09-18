from typing import Optional

class AutoclickerError(Exception):
    """Base exception class for all autoclicker issues."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when the autoclicker configuration is invalid."""
    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        self.config_key = config_key
        super().__init__(f"Configuration error at {config_key}: {message}" if config_key else message)

class ClickExecutionError(AutoclickerError):
    """Raised when a mouse click event fails to trigger."""
    def __init__(self, x: int, y: int, reason: str) -> None:
        self.x = x
        self.y = y
        super().__init__(f"Failed to click at ({x}, {y}): {reason}")

class InputMappingError(AutoclickerError):
    """Raised when input key mappings cannot be parsed."""
    def __init__(self, key_code: str) -> None:
        super().__init__(f"Invalid or unsupported key mapping: {key_code}")

class ProcessInterrupt(AutoclickerError):
    """Raised when the autoclicker process is manually stopped."""
    def __init__(self, message: str = "Execution interrupted by user") -> None:
        super().__init__(message)