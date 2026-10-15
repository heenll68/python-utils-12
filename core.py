import time
import logging
import functools
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying network functions on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying...")
                    if attempt < max_attempts:
                        time.sleep(delay * attempt)
            logger.error("Max retries reached. Operation failed.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2.0)
def perform_click_sync(target_url: str):
    """Example network call for the autoclicker core."""
    # Simulating network activity for the clicker
    print(f"Attempting connection to {target_url}...")
    raise ConnectionError("Server unreachable")