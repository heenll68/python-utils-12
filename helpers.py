import time
import pyautogui
from typing import Tuple

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    """Performs a click at specific coordinates with delay."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def get_mouse_position() -> Tuple[int, int]:
    """Returns the current screen coordinates of the mouse."""
    return pyautogui.position()

def wait_for_input(seconds: float) -> None:
    """Pauses execution for a specified duration."""
    time.sleep(seconds)

def perform_drag(start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.5) -> None:
    """Drags the mouse from one point to another."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=duration)

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if coordinates are within screen boundaries."""
    return 0 <= x < screen_width and 0 <= y < screen_height

def emergency_stop() -> None:
    """Aborts all operations via fail-safe move."""
    pyautogui.FAILSAFE = True