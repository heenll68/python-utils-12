import logging
import pyautogui

logger = logging.getLogger(__name__)

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with boundary and failure handling."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        # Validate coordinates are within screen bounds
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            logger.error(f"Coordinates ({x}, {y}) out of screen bounds")
            return False
            
        pyautogui.click(x=x, y=y)
        return True
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered by user")
        return False
    except Exception as e:
        logger.error(f"Unexpected clicking error: {e}")
        return False

def validate_interval(value: float) -> float:
    """Ensures interval is within sane operational limits."""
    try:
        val = float(value)
        if val < 0.01:
            logger.warning("Interval too low, defaulting to 0.01s")
            return 0.01
        return val
    except (ValueError, TypeError):
        logger.error("Invalid interval format, defaulting to 1.0s")
        return 1.0