import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator for retrying network operations on failure.
    
    Args:
        max_attempts: Maximum number of attempts before raising exception.
        delay: Seconds to wait between attempts.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"Operation failed after {max_attempts} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(max_attempts=3, delay=2.0)
def fetch_remote_config(url: str):
    """
    Example network operation placeholder to fetch autoclicker config.
    """
    # In real usage, this would wrap requests.get(url)
    raise ConnectionError("Failed to connect to update server")