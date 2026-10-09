import functools
import time
from typing import Callable, Any

# Cache for performance optimization of validator calls
_validator_cache = {}

def memoize_validator(func: Callable) -> Callable:
    """Cache validator results to reduce redundant checks in high-speed loops."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _validator_cache:
            _validator_cache[key] = func(*args, **kwargs)
        return _validator_cache[key]
    return wrapper

@memoize_validator
def validate_click_interval(interval: float) -> bool:
    """Ensures click interval is within hardware safety limits."""
    return 0.001 <= interval <= 60.0

def clear_validator_cache() -> None:
    """Clears memory for the validator cache during config reload."""
    _validator_cache.clear()

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Bounds checking for click coordinates."""
    return (0 <= x < screen_width) and (0 <= y < screen_height)