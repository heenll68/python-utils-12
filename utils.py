import time
import logging
import pyautogui

# Configure logging for autoclicker operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('autoclicker')

def perform_click(x: int, y: int, interval: float = 0.1):
    """Execute a mouse click at target coordinates."""
    try:
        pyautogui.click(x, y)
        time.sleep(interval)
    except Exception as e:
        logger.error(f"failed click at ({x}, {y}): {e}")

def get_mouse_position():
    """Retrieve current cursor coordinates."""
    return pyautogui.position()

def safe_exit(message: str = "shutdown initiated"):
    """Log shutdown and terminate execution."""
    logger.info(message)
    exit(0)

class ClickCoordinator:
    """Manages repetition logic for mouse clicks."""
    def __init__(self, repeat: int = 1):
        self.repeat = repeat

    def run_sequence(self, x: int, y: int):
        for i in range(self.repeat):
            logger.info(f"execution cycle {i+1}/{self.repeat}")
            perform_click(x, y)
