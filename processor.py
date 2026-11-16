import time
import random
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries=3, delay=1.0, backoff=2.0):
    """Decorator to implement exponential backoff for network operations."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    sleep_time = current_delay + random.uniform(0, 0.1)
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_on_failure(max_retries=3)
def execute_network_request(data):
    """Example function performing a network operation."""
    # Simulating a volatile network connection
    if random.random() < 0.7:
        raise ConnectionError("Network connection lost")
    return f"Successfully processed: {data}"