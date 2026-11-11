import time
import logging
from typing import Callable, Any, Tuple
import urllib.error
import urllib.request

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: Tuple[type[BaseException], ...] = (urllib.error.URLError, TimeoutError, ConnectionError)
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff.
    Designed for autoclicker remote profile syncing and update checks.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation {func.__name__} failed after {max_retries} attempts: {err}"
                        )
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for {func.__name__} failed ({err}). "
                        f"Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator


@retry_network_op(max_retries=3, backoff_factor=2.0)
def fetch_remote_preset(url: str, timeout: float = 5.0) -> str:
    """Fetch autoclicker preset configuration from a remote URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "AutoClicker-Utils/1.2"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8")
