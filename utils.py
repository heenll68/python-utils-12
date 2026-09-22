import time
import pyautogui
from typing import Tuple

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    """Performs a mouse click at coordinates with a safety delay."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def get_mouse_position() -> Tuple[int, int]:
    """Retrieves current screen coordinates of the mouse cursor."""
    return pyautogui.position()

def debounce_input(last_time: float, threshold: float = 0.5) -> bool:
    """Checks if enough time has passed since last action."""
    return (time.time() - last_time) > threshold

def format_coordinates(x: int, y: int) -> str:
    """Formats coordinates for logging purposes."""
    return f"X: {x}, Y: {y}"

def sleep_with_check(seconds: float, stop_event=None) -> bool:
    """Sleeps while periodically checking for a stop signal."""
    end_time = time.time() + seconds
    while time.time() < end_time:
        if stop_event and stop_event.is_set():
            return False
        time.sleep(0.05)
    return True