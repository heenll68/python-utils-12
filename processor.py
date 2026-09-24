import time
import random
import pyautogui

def perform_click(x: int, y: int, interval: float = 0.0) -> None:
    """Executes a mouse click at target coordinates."""
    pyautogui.click(x, y)
    if interval > 0:
        time.sleep(interval)

def random_jitter(x: int, y: int, range_px: int = 5) -> tuple[int, int]:
    """Applies small random offset to coordinates to mimic human behavior."""
    dx = random.randint(-range_px, range_px)
    dy = random.randint(-range_px, range_px)
    return (x + dx, y + dy)

def smart_sleep(min_sec: float, max_sec: float) -> None:
    """Pauses execution for a random duration within a range."""
    duration = random.uniform(min_sec, max_sec)
    time.sleep(duration)

def validate_screen_bounds(x: int, y: int) -> bool:
    """Verifies if target coordinates are within active display."""
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height

def click_sequence(coordinates: list[tuple[int, int]], delay: float = 0.1) -> None:
    """Iterates through a list of coordinates to perform clicks."""
    for x, y in coordinates:
        if validate_screen_bounds(x, y):
            perform_click(x, y, delay)
