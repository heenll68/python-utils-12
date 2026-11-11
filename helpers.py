import time
import pyautogui
import random

def safe_click(x: int, y: int, interval: float = 0.05) -> None:
    """Performs a mouse click at coordinates with a randomized delay."""
    delay = interval + random.uniform(0, 0.02)
    time.sleep(delay)
    pyautogui.click(x, y)

def wait_for_ready(seconds: int = 1) -> None:
    """Pauses execution to allow user prep time."""
    print(f"Starting in {seconds} seconds...")
    time.sleep(seconds)

def get_random_offset(radius: int = 5) -> tuple:
    """Generates small coordinate variations to evade detection."""
    dx = random.randint(-radius, radius)
    dy = random.randint(-radius, radius)
    return dx, dy

def perform_humanized_click(x: int, y: int) -> None:
    """Click with positional jitter to mimic human behavior."""
    dx, dy = get_random_offset()
    safe_click(x + dx, y + dy)

def toggle_clicker_state(current_state: bool) -> bool:
    """Flips the active state of the autoclicker."""
    return not current_state