import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_attempts=3, delay=2):
    """Decorator to retry network functions on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"Operation failed after {max_attempts} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(max_attempts=3, delay=1)
def perform_network_click(endpoint):
    """Example network call for the autoclicker."""
    # Simulating actual network I/O
    logger.info(f"Sending click event to {endpoint}")
    return True