import time
import pyautogui
import random

def execute_click(x: int, y: int, interval: float = 0.1):
    """Performs a mouse click at target coordinates."""
    pyautogui.click(x, y)
    time.sleep(interval)

def execute_randomized_click(x: int, y: int, jitter: int = 5):
    """Performs a click with minor spatial randomization."""
    rx = x + random.randint(-jitter, jitter)
    ry = y + random.randint(-jitter, jitter)
    pyautogui.click(rx, ry)

def get_screen_bounds():
    """Returns the primary monitor dimensions."""
    return pyautogui.size()

def wait_for_ready(seconds: int = 3):
    """Provides a countdown delay before execution."""
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

def safe_move(x: int, y: int, duration: float = 0.25):
    """Moves mouse cursor to coordinates safely."""
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)

def perform_sequence(coordinates: list, delay: float = 0.5):
    """Executes clicks in a predefined list of points."""
    for x, y in coordinates:
        execute_click(x, y)
        time.sleep(delay)