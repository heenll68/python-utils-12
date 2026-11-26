import functools
import time
from typing import Callable, Any

# Cache click validation results to reduce overhead in tight loops
_validation_cache = {}

def lru_cache_with_ttl(seconds: int = 1):
    def decorator(func: Callable):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            key = (args, tuple(kwargs.items()))
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < seconds:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

@lru_cache_with_ttl(seconds=0.5)
def validate_click_bounds(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Ensures coordinates stay within current display bounds."""
    return 0 <= x < screen_width and 0 <= y < screen_height

def sanitize_interval(interval: float) -> float:
    """Enforce a minimum safe interval for CPU efficiency."""
    return max(0.001, float(interval))

# Validation batch handler for bulk input checks
def validate_batch(coordinates: list, width: int, height: int) -> list:
    """Filter invalid coordinates using cached validation."""
    return [coord for coord in coordinates if validate_click_bounds(coord[0], coord[1], width, height)]