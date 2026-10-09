import time
import random
import pyautogui

def safe_click(x, y, delay=0.1):
    """Perform a click with random jitter and safety delay."""
    jitter_x = random.randint(-2, 2)
    jitter_y = random.randint(-2, 2)
    pyautogui.moveTo(x + jitter_x, y + jitter_y)
    pyautogui.click()
    time.sleep(delay)

def wait_for_seconds(base_seconds, variance=0.2):
    """Pause execution for a random time interval."""
    sleep_time = base_seconds + random.uniform(-variance, variance)
    time.sleep(max(0, sleep_time))

def get_screen_center():
    """Calculate the center point of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def is_in_bounds(x, y):
    """Validate if coordinates are within screen dimensions."""
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height

def drag_to(start_x, start_y, end_x, end_y, duration=0.5):
    """Execute a smooth drag operation between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, tween=pyautogui.easeInOutQuad)