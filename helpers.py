import random
import re
from typing import Tuple


def calculate_jitter(base_interval: float, variance: float = 0.15) -> float:
    """Calculate a humanized delay interval with random jitter variance."""
    if base_interval <= 0:
        return 0.0
    delta = base_interval * variance
    delay = random.uniform(base_interval - delta, base_interval + delta)
    return max(0.001, delay)


def clamp_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> Tuple[int, int]:
    """Ensure target click coordinates stay within display bounds."""
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))
    return clamped_x, clamped_y


def parse_interval(interval_str: str) -> float:
    """Parse time interval string (e.g., '250ms', '1.5s', '2m') into seconds."""
    match = re.match(r"^(\d+(?:\.\d+)?)\s*(ms|s|m|h)?$", interval_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid interval format: '{interval_str}'")

    value, unit = match.groups()
    num = float(value)

    if unit == "ms":
        return num / 1000.0
    elif unit == "m":
        return num * 60.0
    elif unit == "h":
        return num * 3600.0
    return num


def format_duration(seconds: float) -> str:
    """Format total elapsed seconds into a standard HH:MM:SS string."""
    total_sec = int(seconds)
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    secs = total_sec % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
