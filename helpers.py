import logging

def validate_click_settings(interval: float, duration: float, iterations: int) -> bool:
    """Validates autoclicker parameters to ensure system stability."""
    try:
        if interval < 0.01:
            logging.error("Interval too low: minimum is 0.01s")
            return False
        if duration < 0:
            logging.error("Duration cannot be negative")
            return False
        if iterations < 0:
            logging.error("Iterations must be zero or positive")
            return False
        return True
    except TypeError:
        logging.error("Invalid input types provided for settings")
        return False

def sanitize_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
    """Clamps coordinates to current screen boundaries."""
    safe_x = max(0, min(x, screen_width))
    safe_y = max(0, min(y, screen_height))
    return safe_x, safe_y

def log_validation_error(message: str) -> None:
    """Standardized logging for input validation failures."""
    logging.warning(f"Validation failure: {message}")