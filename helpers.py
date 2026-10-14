import logging
import pyautogui
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

def get_safe_coordinates(x: int, y: int) -> Optional[Tuple[int, int]]:
    """Validates coordinates against current screen resolution."""
    try:
        screen_width, screen_height = pyautogui.size()
        if 0 <= x <= screen_width and 0 <= y <= screen_height:
            return (x, y)
        logger.warning(f"Coordinates ({x}, {y}) out of screen bounds ({screen_width}x{screen_height}).")
        return None
    except Exception as e:
        logger.error(f"Unexpected error during coordinate validation: {e}")
        return None

def perform_safe_click(x: int, y: int, clicks: int = 1) -> bool:
    """Executes click only if coordinates are confirmed safe."""
    coords = get_safe_coordinates(x, y)
    if coords:
        try:
            pyautogui.click(x=coords[0], y=coords[1], clicks=clicks)
            return True
        except pyautogui.FailSafeException:
            logger.critical("Autoclicker fail-safe triggered by user.")
            return False
        except Exception as e:
            logger.error(f"Click failure at ({x}, {y}): {e}")
            return False
    return False