import random
import time
from typing import Tuple


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to a delay interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def calculate_jittered_delay(base_interval: float, jitter_percent: float = 0.1) -> float:
    """Apply a random jitter percentage to the base interval to simulate human clicking."""
    if base_interval < 0:
        raise ValueError("Base interval cannot be negative.")
    jitter_percent = max(0.0, min(1.0, jitter_percent))
    delta = base_interval * jitter_percent
    return max(0.001, random.uniform(base_interval - delta, base_interval + delta))


def clamp_coordinates(x: int, y: int, max_x: int, max_y: int) -> Tuple[int, int]:
    """Clamp target screen coordinates within valid screen boundaries."""
    clamped_x = max(0, min(x, max_x))
    clamped_y = max(0, min(y, max_y))
    return clamped_x, clamped_y


def format_elapsed_time(seconds: float) -> str:
    """Format total elapsed seconds into a readable string (HH:MM:SS or MM:SS)."""
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"
