import time
import pyautogui
from typing import Tuple, Optional

class ClickHandler:
    """Handles automated mouse click operations with safety boundaries."""

    def __init__(self, interval: float = 0.1, failsafe: bool = True) -> None:
        self.interval: float = interval
        pyautogui.FAILSAFE = failsafe

    def perform_click(self, coordinates: Tuple[int, int]) -> bool:
        """Executes a left click at the specified (x, y) coordinates."""
        try:
            x, y = coordinates
            pyautogui.click(x=x, y=y)
            time.sleep(self.interval)
            return True
        except (pyautogui.FailSafeException, pyautogui.PyAutoGUIException) as e:
            print(f"Click failed: {e}")
            return False

    def get_screen_dimensions(self) -> Tuple[int, int]:
        """Returns the current screen resolution as (width, height)."""
        return pyautogui.size()

    def validate_bounds(self, x: int, y: int) -> bool:
        """Checks if coordinates are within screen boundaries."""
        width, height = self.get_screen_dimensions()
        return 0 <= x < width and 0 <= y < height