import time
import pyautogui
import logging

logger = logging.getLogger(__name__)

def execute_click(x: int, y: int, interval: float = 0.1):
    """Performs a mouse click with input validation and safety checks."""
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers")
        
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
        
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered by user. Stopping execution.")
        raise
    except ValueError as e:
        logger.error(f"Input validation error: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error during click execution: {e}")

def batch_click_processor(tasks: list):
    """Processes a list of coordinate tuples for automated clicking."""
    if not tasks:
        logger.warning("Empty task list provided.")
        return

    for task in tasks:
        try:
            x, y = task
            execute_click(x, y)
        except (TypeError, ValueError):
            logger.error(f"Skipping malformed task: {task}")
            continue