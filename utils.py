from __future__ import annotations

import time

import random

import pyautogui

def get_random_delay(min_delay: float, max_delay: float) -> float:
    """Return random delay between min and max seconds."""
    return random.uniform(min_delay, max_delay)

def simulate_click(x: int, y: int, button: str = 'left') -> None:
    """Move to position and click the mouse button."""
    pyautogui.moveTo(x, y, duration=0.1)
    if button == 'left':
        pyautogui.click(x, y)
    elif button == 'right':
        pyautogui.click(x, y, button='right')

def add_position_jitter(x: int, y: int, amount: int = 3) -> tuple[int, int]:
    """Add small random offset to coordinates."""
    new_x = x + random.randint(-amount, amount)
    new_y = y + random.randint(-amount, amount)
    return new_x, new_y

def human_click_sequence(x: int, y: int, num_clicks: int = 1) -> None:
    """Perform a sequence of clicks with human-like delays."""
    for _ in range(num_clicks):
        jitter_x, jitter_y = add_position_jitter(x, y)
        simulate_click(jitter_x, jitter_y)
        time.sleep(get_random_delay(0.05, 0.15))

def validate_coordinates(x: int, y: int) -> bool:
    """Check if coordinates are valid positive integers."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0