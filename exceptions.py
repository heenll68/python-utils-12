class AutoclickerError(Exception):
    """Base exception for all autoclicker issues."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when settings are invalid or missing."""
    pass

class PermissionDeniedError(AutoclickerError):
    """Raised when OS prevents input injection."""
    pass

class CoordinateOutOfBoundsError(AutoclickerError):
    """Raised when click target is off-screen."""
    pass

class ProcessInterruptError(AutoclickerError):
    """Raised when autoclicker loop is forced stop."""
    pass

def raise_if_invalid(condition: bool, message: str, exception_cls: type = AutoclickerError):
    """Utility to raise custom exceptions based on boolean checks."""
    if not condition:
        raise exception_cls(message)

def handle_critical_failure(e: Exception):
    """Standardized logging for application crashes."""
    print(f"[CRITICAL] {type(e).__name__}: {e}")
    raise e