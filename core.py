import time
import pyautogui
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def perform_click(x, y, interval=0.1):
    """Executes a click at screen coordinates with safety boundaries."""
    try:
        # Screen dimensions validation
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) outside screen bounds ({screen_width}x{screen_height})")

        # Fail-safe check
        pyautogui.FAILSAFE = True
        
        # Execute action
        pyautogui.click(x, y)
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered: mouse moved to corner")
        raise
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid click parameters: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during click: {e}")

def run_autoclicker(target_coords, iterations=100):
    """Main loop handler with error suppression."""
    for i in range(iterations):
        try:
            perform_click(*target_coords)
        except Exception as e:
            logger.warning(f"Iteration {i} failed: {e}. Skipping.")
            continue