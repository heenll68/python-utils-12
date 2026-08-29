"""Custom exceptions and error handling for autoclicker edge cases."""

import sys

class AutoclickerError(Exception):
    """Base exception for autoclicker errors."""
    pass

class InvalidClickIntervalError(AutoclickerError):
    """Raised when the click interval is invalid or too small."""
    def __init__(self, interval, min_interval=0.01):
        self.interval = interval
        self.min_interval = min_interval
        super().__init__(f"Invalid click interval: {interval}. Must be at least {min_interval}.")

class ScreenOutOfBoundsError(AutoclickerError):
    """Raised when click coordinates are outside screen boundaries."""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(f"Position ({x}, {y}) out of screen bounds ({width}x{height}).")

class AutoclickerPermissionError(AutoclickerError):
    """Raised when mouse control permission is denied."""
    def __init__(self, message="Mouse control permission denied."):
        super().__init__(message)

class InvalidClickCountError(AutoclickerError):
    """Raised when click count is not positive."""
    def __init__(self, count):
        self.count = count
        super().__init__(f"Click count must be positive, received {count}.")

def handle_error(error):
    """Central error handler for autoclicker edge cases."""
    if isinstance(error, InvalidClickIntervalError):
        print(f"Warning: {error}. Using minimum interval.")
        return error.min_interval
    elif isinstance(error, ScreenOutOfBoundsError):
        print(f"Warning: {error}. Clamping to bounds.")
        new_x = max(0, min(error.x, error.width - 1))
        new_y = max(0, min(error.y, error.height - 1))
        return new_x, new_y
    elif isinstance(error, AutoclickerPermissionError):
        print("Error: Permission denied. Exiting.")
        sys.exit(1)
    elif isinstance(error, InvalidClickCountError):
        print(f"Warning: {error}. Using 1 click.")
        return 1
    else:
        print(f"Unexpected error: {error}")
        raise error

if __name__ == "__main__":
    try:
        interval = 0.005
        if interval < 0.01:
            raise InvalidClickIntervalError(interval)
    except AutoclickerError as e:
        fixed = handle_error(e)
        print(f"Proceeding with interval: {fixed}")
    try:
        x, y = 2000, 1500
        w, h = 1920, 1080
        if x >= w or y >= h:
            raise ScreenOutOfBoundsError(x, y, w, h)
    except AutoclickerError as e:
        fixed = handle_error(e)
        print(f"Using clamped position: {fixed}")