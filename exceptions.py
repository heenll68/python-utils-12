class AutoclickerError(Exception):
    """Base exception for all autoclicker issues."""

class ConfigurationError(AutoclickerError):
    """Raised when settings are invalid."""

class HardwareControlError(AutoclickerError):
    """Raised when input injection fails."""

class ProcessInterruptError(AutoclickerError):
    """Raised when execution is force-stopped."""

def validate_interval(interval: float) -> None:
    """Ensures click interval is within safe bounds."""
    if not isinstance(interval, (int, float)):
        raise ConfigurationError(f"Invalid type: {type(interval)}")
    if interval < 0.01:
        raise ConfigurationError("Interval below 10ms threshold")

def handle_control_exception(err: Exception) -> None:
    """Centralized error reporting for input operations."""
    if isinstance(err, HardwareControlError):
        print(f"Critical hardware failure: {err}")
    elif isinstance(err, ConfigurationError):
        print(f"Configuration safety violation: {err}")
    else:
        print(f"Unexpected autoclicker runtime error: {err}")