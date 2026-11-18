import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

def validate_connection_status(func):
    """Validator ensuring target is reachable before clicking actions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Simulation of reachability check
        if not hasattr(args[0], 'is_connected') or not args[0].is_connected():
            raise ConnectionError("Network interface not ready for click input")
        return func(*args, **kwargs)
    return wrapper