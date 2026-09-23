import time
from typing import Callable, Any
from functools import lru_cache

class ClickValidator:
    """High-performance validation layer for autoclicker inputs."""
    
    def __init__(self, debounce_ms: int = 10):
        self.debounce_ms = debounce_ms / 1000.0
        self._last_call = 0.0

    @lru_cache(maxsize=128)
    def is_valid_coordinate(self, x: int, y: int, screen_width: int, screen_height: int) -> bool:
        """Check if coordinate falls within monitor bounds using cache."""
        return 0 <= x < screen_width and 0 <= y < screen_height

    def rate_limit(func: Callable) -> Callable:
        """Decorator to throttle click execution frequency."""
        def wrapper(self, *args, **kwargs):
            current_time = time.perf_counter()
            if current_time - self._last_call < self.debounce_ms:
                return False
            self._last_call = current_time
            return func(self, *args, **kwargs)
        return wrapper

    def validate_interval(self, interval: float) -> float:
        """Ensure click frequency is within hardware safety limits."""
        return max(0.001, min(interval, 60.0))

def get_validator_instance(debounce: int = 10) -> ClickValidator:
    """Factory for persistent validator instance."""
    return ClickValidator(debounce_ms=debounce)