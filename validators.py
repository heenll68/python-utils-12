import re

def validate_coordinates(x: int, y: int) -> bool:
    """Verify that coordinates are non-negative integers."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    """Ensure the click interval is a valid positive duration."""
    return isinstance(interval, (int, float)) and interval > 0

def validate_button(button: str) -> bool:
    """Validate mouse button strings for input processing."""
    valid_buttons = {'left', 'right', 'middle'}
    return str(button).lower() in valid_buttons

def parse_hotkey_sequence(sequence: str) -> bool:
    """Validate key binding format using regex patterns."""
    pattern = r'^([a-z]+)(\+[a-z]+)*$'
    return bool(re.match(pattern, sequence.lower()))

def check_bounds(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Verify coordinates fall within screen resolution."""
    return 0 <= x <= screen_width and 0 <= y <= screen_height