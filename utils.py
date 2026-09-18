import time
import pyautogui
from typing import Tuple, Optional

def perform_click(x: int, y: int, interval: float = 0.0) -> None:
    """Executes a mouse click at the specified coordinates.

    Args:
        x: Horizontal coordinate.
        y: Vertical coordinate.
        interval: Seconds to wait after clicking.
    """
    pyautogui.click(x, y)
    if interval > 0:
        time.sleep(interval)

def get_mouse_position() -> Tuple[int, int]:
    """Retrieves the current mouse cursor location.

    Returns:
        A tuple containing (x, y) coordinates.
    """
    return pyautogui.position()

def safe_move(x: int, y: int, duration: float = 0.25) -> None:
    """Smoothly moves the mouse to target coordinates.

    Args:
        x: Destination x coordinate.
        y: Destination y coordinate.
        duration: Time taken to reach the destination.
    """
    pyautogui.moveTo(x, y, duration=duration)

def validate_screen_bounds(x: int, y: int) -> bool:
    """Checks if coordinates are within primary monitor limits.

    Args:
        x: Horizontal coordinate.
        y: Vertical coordinate.

    Returns:
        True if coordinates are visible on screen.
    """
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height