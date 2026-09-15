import time
from functools import lru_cache

@lru_cache(maxsize=128)
def get_normalized_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple:
    """Cache coordinate normalization to reduce floating point math in hot loops."""
    nx = max(0, min(1, x / screen_width))
    ny = max(0, min(1, y / screen_height))
    return (nx, ny)

def throttle_click_events(interval_ms: int):
    """Decorator to prevent click spamming beyond specified frequency."""
    last_called = [0.0]

    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - last_called[0]) >= (interval_ms / 1000.0):
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def calculate_dynamic_delay(base_delay: float, jitter: float) -> float:
    """Simulate human timing variance to bypass basic detection."""
    import random
    return base_delay + random.uniform(-jitter, jitter)

class ClickPerformanceTimer:
    """Context manager for tracking click execution latency."""
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start