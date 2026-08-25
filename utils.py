import time
import random
from typing import Tuple, List

def random_delay(min_seconds: float, max_seconds: float) -> float:
    """Return a random float delay between the given min and max."""
    if min_seconds < 0 or max_seconds < 0:
        raise ValueError("Delays must be non-negative")
    return random.uniform(min_seconds, max_seconds)

def sleep_jitter(base: float, percent: float = 0.2) -> None:
    """Sleep base time with random jitter percentage."""
    variation = base * random.uniform(-percent, percent)
    time.sleep(max(0.001, base + variation))

def random_coordinates(x_min: int, x_max: int, y_min: int, y_max: int) -> Tuple[int, int]:
    """Provide random x y within specified rectangular area."""
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    return x, y

def click_intervals(total_clicks: int, avg_interval: float) -> List[float]:
    """Generate list of intervals for a number of clicks."""
    intervals = []
    for _ in range(total_clicks - 1):
        jittered = avg_interval * random.uniform(0.7, 1.3)
        intervals.append(max(0.05, jittered))
    return intervals

def execute_autoclick(clicks: int, delay: float) -> None:
    """Run simulated autoclick sequence using the helpers."""
    if clicks < 1:
        return
    print("Starting autoclick sequence")
    for i in range(clicks):
        print(f"Click number {i + 1}")
        sleep_jitter(delay)
    print("Sequence completed")

if __name__ == "__main__":
    print(random_delay(0.1, 0.3))
    sleep_jitter(0.5)
    print(random_coordinates(0, 1920, 0, 1080))
    print(click_intervals(5, 0.5))
    execute_autoclick(3, 0.2)