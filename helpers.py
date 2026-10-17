import time
import random
from typing import Tuple

def get_jittered_interval(base_interval: float, variance: float = 0.1) -> float:
    """Calculate a random interval based on base and variance percentage."""
    min_val = base_interval * (1 - variance)
    max_val = base_interval * (1 + variance)
    return random.uniform(min_val, max_val)

def format_click_position(x: int, y: int) -> str:
    """Return human readable coordinates string."""
    return f"({x}, {y})"

def throttle_execution(interval: float) -> None:
    """Pause execution to respect timing constraints."""
    time.sleep(interval)

def validate_coordinates(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    """Check if coordinates are within screen boundaries."""
    width, height = screen_size
    return 0 <= x < width and 0 <= y < height