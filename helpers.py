import random
import math
from typing import Tuple


def calculate_random_delay(base_interval: float, jitter: float = 0.1) -> float:
    """Calculate a humanized delay by adding Gaussian noise to base interval."""
    if base_interval <= 0:
        return 0.0
    
    # Standard deviation based on jitter percentage
    sigma = base_interval * max(0.0, min(jitter, 1.0))
    delay = random.gauss(base_interval, sigma)
    
    # Ensure delay doesn't fall below a safe threshold
    return max(0.001, delay)


def convert_cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to interval duration in seconds."""
    if cps <= 0:
        raise ValueError("CPS value must be greater than zero")
    return 1.0 / cps


def clamp_coordinates(x: int, y: int, screen_bounds: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Ensure click coordinates fall within the specified screen bounding box."""
    min_x, min_y, max_x, max_y = screen_bounds
    
    clamped_x = max(min_x, min(x, max_x))
    clamped_y = max(min_y, min(y, max_y))
    
    return clamped_x, clamped_y


def format_elapsed_time(seconds: float) -> str:
    """Format elapsed seconds into a human-readable HH:MM:SS string."""
    total_seconds = int(math.floor(seconds))
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"