import time
import logging
import urllib.error
import urllib.request
from typing import Callable, Any, Tuple

logger = logging.getLogger(__name__)


def retry_network_operation(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    exceptions: Tuple[type[Exception], ...] = (urllib.error.URLError, TimeoutError, ConnectionError)
):
    """
    Decorator to retry network requests with exponential backoff for autoclicker syncing.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error("Network request failed after %d attempts: %s", max_retries, exc)
                        raise
                    
                    delay = backoff_factor * (2 ** (attempts - 1))
                    logger.warning(
                        "Network error encountered: %s. Retrying in %.2fs (Attempt %d/%d)",
                        exc, delay, attempts, max_retries
                    )
                    time.sleep(delay)
        return wrapper
    return decorator


@retry_network_operation(max_retries=3, backoff_factor=0.5)
def fetch_remote_config(url: str, timeout: int = 5) -> str:
    """
    Fetches remote autoclicker configuration or update metadata.
    """
    req = urllib.request.Request(url, headers={"User-Agent": "AutoClicker/12.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8")
