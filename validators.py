class ValidationError(Exception):
    """Custom exception for input validation failures in autoclicker."""
    pass

def validate_click_params(interval: float, count: int) -> None:
    """Ensures click parameters are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValidationError(f"Invalid interval: {interval}. Must be >= 0.01s")
    
    if not isinstance(count, int) or (count < -1):
        raise ValidationError(f"Invalid count: {count}. Must be -1 (infinite) or > 0")

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> None:
    """Verifies target coordinates fall within screen boundaries."""
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise ValidationError(f"Coordinates ({x}, {y}) out of screen bounds")

def sanitize_input(value: str, default: int) -> int:
    """Attempts to parse integer input with a fallback mechanism."""
    try:
        parsed = int(value)
        return parsed if parsed > 0 else default
    except (ValueError, TypeError):
        return default