import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to retry network-dependent functions with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

def validate_connection_status(status_code: int) -> bool:
    """
    Checks if the status code indicates a successful network response.
    """
    return 200 <= status_code < 300