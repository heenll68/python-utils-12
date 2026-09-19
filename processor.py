import time
import pyautogui
import random

def perform_click(x, y, interval=0.1):
    """Execute a mouse click at target coordinates."""
    pyautogui.click(x, y)
    time.sleep(interval)

def perform_drag(start_x, start_y, end_x, end_y, duration=0.5):
    """Execute a drag operation between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button='left')

def wait_random(min_sec=0.5, max_sec=2.0):
    """Introduce a random delay to mimic human behavior."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def get_screen_center():
    """Calculate the center of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def safe_exit_check():
    """Verify emergency stop condition via mouse position."""
    x, y = pyautogui.position()
    if x == 0 and y == 0:
        raise InterruptedError("Emergency stop triggered at screen corner")