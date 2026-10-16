import time
import pyautogui
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def perform_click(x: int, y: int, interval: float = 0.1) -> None:
    """Executes a mouse click at specified screen coordinates."""
    try:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered, stopping execution")
        raise
    except Exception as e:
        logger.error(f"Click failure at ({x}, {y}): {e}")

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are within the primary monitor bounds."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height

def safe_shutdown(delay: int = 2) -> None:
    """Graceful shutdown sequence for the autoclicker."""
    logger.info("Initiating shutdown sequence...")
    time.sleep(delay)
    exit(0)