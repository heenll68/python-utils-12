import time
import pyautogui
from typing import Tuple, Optional

def perform_click(position: Tuple[int, int], interval: float = 0.1) -> bool:
    """
    Executes a mouse click at the specified coordinate.

    Args:
        position: A tuple of (x, y) coordinates.
        interval: Time to wait before clicking in seconds.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        pyautogui.moveTo(position[0], position[1])
        time.sleep(interval)
        pyautogui.click()
        return True
    except pyautogui.FailSafeException:
        return False

def get_mouse_position() -> Tuple[int, int]:
    """
    Retrieves the current cursor coordinates.

    Returns:
        Tuple[int, int]: The (x, y) coordinates of the mouse.
    """
    return pyautogui.position()

def safe_sleep(seconds: float) -> None:
    """
    Pauses execution for a set duration.

    Args:
        seconds: The duration in seconds.
    """
    time.sleep(seconds)