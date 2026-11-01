import random
import time
from typing import Tuple


def calculate_jitter_delay(base_delay: float, max_jitter: float = 0.05) -> float:
    """Calculate a humanized click delay by adding random jitter to base delay.
    
    Args:
        base_delay: Target delay in seconds between clicks.
        max_jitter: Maximum variation in seconds added or subtracted.
        
    Returns:
        A positive float representing the randomized delay duration.
    """
    jitter = random.uniform(-max_jitter, max_jitter)
    return max(0.001, base_delay + jitter)


def clamp_coordinates(x: int, y: int, screen_bounds: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Clamp target coordinates to ensure they remain within the specified screen boundary.
    
    Args:
        x: X-coordinate position.
        y: Y-coordinate position.
        screen_bounds: Tuple of (min_x, min_y, max_x, max_y).
        
    Returns:
        Tuple of safe (x, y) coordinates within bounds.
    """
    min_x, min_y, max_x, max_y = screen_bounds
    clamped_x = max(min_x, min(x, max_x))
    clamped_y = max(min_y, min(y, max_y))
    return clamped_x, clamped_y


def generate_random_point(top_left: Tuple[int, int], width: int, height: int) -> Tuple[int, int]:
    """Generate a random coordinate point within a target rectangular area.
    
    Args:
        top_left: (x, y) coordinates of the top-left corner.
        width: Width of the region in pixels.
        height: Height of the region in pixels.
        
    Returns:
        Tuple of (x, y) target click coordinates.
    """
    start_x, start_y = top_left
    rand_x = random.randint(start_x, start_x + max(0, width))
    rand_y = random.randint(start_y, start_y + max(0, height))
    return rand_x, rand_y


def parse_interval(interval_str: str) -> float:
    """Parse a time interval string into total seconds.
    
    Supports formats like '1.5s', '200ms', or plain numeric strings.
    """
    cleaned = interval_str.strip().lower()
    if cleaned.endswith("ms"):
        return float(cleaned[:-2]) / 1000.0
    elif cleaned.endswith("s"):
        return float(cleaned[:-1])
    return float(cleaned)
