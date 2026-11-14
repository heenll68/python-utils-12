import logging

logger = logging.getLogger(__name__)

def validate_click_params(interval, duration):
    """Ensures click parameters are within safe bounds."""
    try:
        val_interval = float(interval)
        val_duration = float(duration)

        if val_interval < 0.01:
            raise ValueError("Interval must be at least 0.01 seconds.")
        if val_duration < 0:
            raise ValueError("Duration cannot be negative.")

        return True, (val_interval, val_duration)
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid input parameters: {e}")
        return False, None

def sanitize_coordinates(x, y):
    """Normalizes coordinate inputs to integers."""
    try:
        return int(x), int(y)
    except (ValueError, TypeError):
        logger.warning(f"Invalid coordinates ({x}, {y}), defaulting to (0, 0)")
        return 0, 0

def is_valid_process_state(state_dict):
    """Checks integrity of the processing dictionary."""
    required = ['active', 'interval', 'duration']
    return all(key in state_dict for key in required) and isinstance(state_dict['active'], bool)