def validate_click_parameters(interval, button):
    """Validates autoclicker parameters before execution."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError(f"Invalid interval: {interval}. Must be >= 0.01 seconds.")
    
    valid_buttons = ['left', 'right', 'middle']
    if button not in valid_buttons:
        raise ValueError(f"Invalid button: {button}. Must be one of {valid_buttons}.")
    
    return True

def validate_coordinates(x, y, screen_width, screen_height):
    """Checks if coordinates fall within screen boundaries."""
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds.")
    return True

def validate_loop_iterations(count):
    """Ensures iteration count is a non-negative integer."""
    if not isinstance(count, int) or count < -1:
        raise ValueError("Iteration count must be -1 (infinite) or a positive integer.")
    return True