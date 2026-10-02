import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=1, backoff=2):
    """Decorator for network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=2)
def ping_server(url):
    """Example network operation function."""
    # Placeholder for actual socket/requests logic
    pass