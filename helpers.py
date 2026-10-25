import functools
import logging
import time
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a network function upon failure using exponential backoff.
    
    Used in autoclicker operations like remote preset sync and update checks.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Network operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise
                    
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed ({err}). "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator


def fetch_remote_presets(url: str, timeout: int = 5) -> dict:
    """
    Fetches remote click presets with built-in network retry logic.
    """
    import urllib.request
    import json

    @retry_network_op(max_retries=3, delay=0.5, exceptions=(Exception,))
    def _request():
        req = urllib.request.Request(url, headers={"User-Agent": "AutoClicker-Utils/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))

    return _request()
