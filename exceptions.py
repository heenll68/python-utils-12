class ClickerError(Exception):
    """Base class for exceptions in the autoclicker module."""
    pass

class ConfigurationError(ClickerError):
    """Raised when there is a configuration issue."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ClickRateError(ClickerError):
    """Raised when an invalid click rate is provided."""
    def __init__(self, rate: float) -> None:
        message = f'Invalid click rate: {rate}'
        super().__init__(message)

class ClickerNotActiveError(ClickerError):
    """Raised when an operation is attempted on an inactive clicker."""
    def __init__(self) -> None:
        message = 'Clicker is not active.'
        super().__init__(message)

class MaxClicksExceededError(ClickerError):
    """Raised when the maximum allowed clicks are exceeded."""
    def __init__(self, max_clicks: int) -> None:
        message = f'Maximum clicks exceeded: {max_clicks}'
        super().__init__(message)
