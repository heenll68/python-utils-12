from typing import Union, Tuple

def validate_coordinates(x: int, y: int) -> bool:
    """Verify that coordinates are within a valid screen range.

    Args:
        x: Horizontal screen coordinate.
        y: Vertical screen coordinate.

    Returns:
        True if coordinates are non-negative, False otherwise.
    """
    return x >= 0 and y >= 0

def validate_interval(interval: Union[int, float]) -> bool:
    """Ensure the click interval is a positive value.

    Args:
        interval: Time in seconds between clicks.

    Returns:
        True if interval is greater than zero, False otherwise.
    """
    return isinstance(interval, (int, float)) and interval > 0

def sanitize_bounds(x: int, y: int, max_x: int, max_y: int) -> Tuple[int, int]:
    """Clamp coordinates to ensure they remain inside screen bounds.

    Args:
        x: Targeted x coordinate.
        y: Targeted y coordinate.
        max_x: Maximum allowed horizontal width.
        max_y: Maximum allowed vertical height.

    Returns:
        Tuple of clamped (x, y) coordinates.
    """
    clamped_x = max(0, min(x, max_x))
    clamped_y = max(0, min(y, max_y))
    return clamped_x, clamped_y