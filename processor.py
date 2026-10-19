import time
import random
import pyautogui

def perform_click(x, y, delay_range=(0.1, 0.5)):
    """Executes a click at coordinates with randomized delay."""
    try:
        pyautogui.moveTo(x, y)
        time.sleep(random.uniform(*delay_range))
        pyautogui.click()
    except Exception as e:
        print(f"Click failure at {x}, {y}: {e}")

def safe_move_and_click(x, y, duration=0.25):
    """Smooth mouse transition to target before clicking."""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def get_random_jitter(offset=5):
    """Generates slight coordinate variations to mimic human behavior."""
    jitter_x = random.randint(-offset, offset)
    jitter_y = random.randint(-offset, offset)
    return jitter_x, jitter_y

def batch_click_sequence(coordinates, interval=1.0):
    """Processes a list of (x, y) tuples with a set pause."""
    for x, y in coordinates:
        perform_click(x, y)
        time.sleep(interval)

def is_screen_region_valid(x, y, width, height):
    """Validates coordinates against current screen resolution."""
    screen_width, screen_height = pyautogui.size()
    return 0 <= x < screen_width and 0 <= y < screen_height