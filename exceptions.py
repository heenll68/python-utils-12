"""Custom exceptions for autoclicker runtime and edge case handling."""


class AutoClickerError(Exception):
    """Base exception class for all autoclicker errors."""

    pass


class InvalidCoordinatesError(AutoClickerError):
    """Raised when target click coordinates are out of bounds or invalid."""

    def __init__(self, x: int, y: int, bounds: tuple[int, int, int, int]):
        self.x = x
        self.y = y
        self.bounds = bounds
        message = f"Coordinates ({x}, {y}) out of screen bounds {bounds}"
        super().__init__(message)


class RateLimitExceededError(AutoClickerError):
    """Raised when requested clicks per second exceed safety limits."""

    def __init__(self, requested_cps: float, max_cps: float = 100.0):
        self.requested_cps = requested_cps
        self.max_cps = max_cps
        message = (
            f"Click rate {requested_cps} CPS exceeds max limit of {max_cps} CPS"
        )
        super().__init__(message)


class WindowNotFoundError(AutoClickerError):
    """Raised when specified target window title is not active or present."""

    def __init__(self, window_title: str):
        self.window_title = window_title
        message = f"Target application window '{window_title}' not found"
        super().__init__(message)


class PermissionDeniedError(AutoClickerError):
    """Raised when OS blocks synthetic input events (e.g. lack of admin privileges)."""

    def __init__(self, action: str = "send click events"):
        message = (
            f"System denied permission to {action}. Try running as admin."
        )
        super().__init__(message)
