import time
import pyautogui
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def perform_click(x: int, y: int, interval: float = 0.1):
    """Executes a safe mouse click at target coordinates."""
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError(f"Coordinates must be integers, got {type(x)}, {type(y)}")
        
        # Safety bounds check for screen resolution
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError("Coordinates out of screen bounds")
            
        pyautogui.click(x, y)
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: mouse moved to corner")
    except ValueError as ve:
        logger.error(f"Invalid input parameters: {ve}")
    except Exception as e:
        logger.error(f"Unexpected clicking error: {e}")

def run_autoclicker(target_coords: list, iterations: int):
    """Main loop execution with error validation."""
    if not target_coords:
        logger.warning("No coordinates provided for clicking sequence")
        return

    for i in range(iterations):
        for x, y in target_coords:
            perform_click(x, y)
        logger.info(f"Completed iteration {i + 1}/{iterations}")