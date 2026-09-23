class ValidationError(Exception):
    """Base class for input validation errors in autoclicker."""
    pass

def validate_click_params(interval: float, count: int) -> None:
    """
    Ensures user inputs for the clicker are within safe and logical bounds.
    
    Args:
        interval: Seconds between clicks (must be positive).
        count: Number of clicks to perform (must be non-negative).
    
    Raises:
        ValidationError: If inputs fail sanity checks.
    """
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValidationError(f"Invalid interval: {interval}. Must be >= 0.01 seconds.")
    
    if not isinstance(count, int) or count < 0:
        raise ValidationError(f"Invalid count: {count}. Must be a non-negative integer.")

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> None:
    """
    Verifies that target click coordinates remain within active display bounds.
    """
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise ValidationError(f"Coordinates ({x}, {y}) outside screen bounds ({screen_width}, {screen_height}).")