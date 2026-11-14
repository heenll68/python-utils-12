import time
import pyautogui
from typing import Tuple

def get_mouse_position() -> Tuple[int, int]:
    """Returns current (x, y) coordinates of the mouse."""
    return pyautogui.position()

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    """Moves to coordinates and performs a click with a safety delay."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def get_screen_resolution() -> Tuple[int, int]:
    """Returns the current primary screen resolution."""
    return pyautogui.size()

def perform_drag(start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.5) -> None:
    """Drags the mouse from start to end coordinates."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=duration, button='left')

def wait_for_seconds(seconds: float) -> None:
    """Blocking sleep wrapper for application throttling."""
    time.sleep(seconds)