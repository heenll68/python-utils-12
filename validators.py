import re

def validate_interval(interval: float) -> bool:
    """Ensures click interval is within safe operating bounds."""
    return 0.01 <= interval <= 60.0

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are non-negative integers."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_hotkey(key: str) -> bool:
    """Validates key input strings using regex."""
    pattern = r'^[a-z0-9_]{1,10}$'
    return bool(re.match(pattern, key.lower()))

def sanitize_input(value: str) -> str:
    """Removes potential whitespace and forces lowercase."""
    return value.strip().lower()

def check_bounds(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Verifies coordinates fall within current screen resolution."""
    return 0 <= x <= screen_width and 0 <= y <= screen_height