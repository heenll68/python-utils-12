import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network-bound functions on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"Function {func.__name__} failed after {max_attempts} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2.0)
def fetch_server_config(url: str):
    """Simulated network request for autoclicker configuration."""
    # Implementation logic for server sync would go here
    pass