class ValidationError(Exception):
    """Base class for autoclicker input validation errors."""
    pass

class ConfigValueError(ValidationError):
    """Raised when user-provided config values are invalid."""
    pass

def validate_click_interval(interval: float):
    """Ensures click interval is within safe operating bounds."""
    if not isinstance(interval, (int, float)):
        raise ConfigValueError(f"Interval must be numeric, got {type(interval).__name__}")
    if interval < 0.01:
        raise ConfigValueError("Interval too low; risk of system instability")
    if interval > 60.0:
        raise ConfigValueError("Interval too high; capping at 60 seconds")

def validate_coordinates(x: int, y: int):
    """Checks if screen coordinates are within expected ranges."""
    if not (0 <= x <= 10000 and 0 <= y <= 10000):
        raise ConfigValueError(f"Coordinates ({x}, {y}) out of realistic screen bounds")

def validate_input_config(data: dict):
    """
    Processes dictionary configuration inputs for the main loop.
    Validates presence and range of required control parameters.
    """
    required = ['interval', 'x', 'y']
    for key in required:
        if key not in data:
            raise ConfigValueError(f"Missing required configuration key: {key}")
    
    validate_click_interval(data['interval'])
    validate_coordinates(data['x'], data['y'])
    return True