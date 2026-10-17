import time
import functools
import logging

# Configure logger for autoclicker network operations
logger = logging.getLogger('python-utils-12')

def retry_network_op(retries=3, delay=2, backoff=2):
    """
    Decorator for retrying network operations with exponential backoff.
    
    :param retries: Number of attempts before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Factor by which the delay increases.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if i == retries - 1:
                        logger.error(f"Final attempt {i+1} failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {i+1} failed for {func.__name__}, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator