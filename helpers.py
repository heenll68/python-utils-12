import random
import time
from typing import Tuple


def calculate_jitter_delay(base_interval: float, max_jitter: float) -> float:
    """Calculate a randomized delay interval to simulate human clicking behavior."""
    if base_interval <= 0:
        return 0.0
    jitter = random.uniform(-max_jitter, max_jitter)
    return max(0.001, base_interval + jitter)


def clamp_coordinates(
    x: int, y: int, screen_width: int, screen_height: int
) -> Tuple[int, int]:
    """Ensure clicking coordinates remain within screen boundaries."""
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))
    return clamped_x, clamped_y


def parse_interval(interval_str: str) -> float:
    """Parse time interval strings into floating point seconds."""
    clean_str = interval_str.strip().lower()
    if clean_str.endswith("ms"):
        return float(clean_str[:-2]) / 1000.0
    elif clean_str.endswith("s"):
        return float(clean_str[:-1])
    return float(clean_str)


class PrecisionTimer:
    """High-precision timer for regulating autoclicker intervals."""

    def __init__(self, interval: float) -> None:
        self.interval = interval
        self._last_time = time.perf_counter()

    def reset(self) -> None:
        """Reset the timer starting reference time."""
        self._last_time = time.perf_counter()

    def should_trigger(self) -> bool:
        """Check if enough time has elapsed for the next action."""
        now = time.perf_counter()
        if now - self._last_time >= self.interval:
            self._last_time = now
            return True
        return False
