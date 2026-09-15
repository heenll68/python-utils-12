class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_click_params(interval: float, count: int):
    """Validates autoclicker configuration parameters."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValidationError("interval must be a float >= 0.01 seconds")
    
    if not isinstance(count, int) or (count < -1):
        raise ValidationError("count must be a positive integer or -1 for infinite")

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int):
    """Ensures click coordinates fall within display bounds."""
    if not (0 <= x <= screen_width) or not (0 <= y <= screen_height):
        raise ValidationError(f"coordinates ({x}, {y}) out of screen bounds")

def sanitize_input(user_input: str) -> str:
    """Basic sanitization for CLI configuration strings."""
    return str(user_input).strip() if user_input else ""