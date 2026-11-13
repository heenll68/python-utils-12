import logging

# Configure logger for module usage
logger = logging.getLogger(__name__)

def validate_click_settings(interval, duration, button):
    """Ensures configuration values are within safe, operable bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logger.error(f"Invalid interval: {interval}. Must be >= 0.01.")
        return False

    if not isinstance(duration, (int, float)) or duration < 0:
        logger.error(f"Invalid duration: {duration}. Must be >= 0.")
        return False

    if button not in ['left', 'right', 'middle']:
        logger.error(f"Invalid button: {button}. Must be left, right, or middle.")
        return False

    return True

def sanitize_coordinates(x, y):
    """Validates that target coordinates are non-negative integers."""
    try:
        x, y = int(x), int(y)
        if x < 0 or y < 0:
            raise ValueError("Coordinates cannot be negative")
        return x, y
    except (ValueError, TypeError):
        logger.warning(f"Invalid coordinates: ({x}, {y}). Using default (0, 0).")
        return 0, 0