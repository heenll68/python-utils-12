import logging
import functools
import time
from typing import Callable, Any

# Configure optimized logging for high-frequency events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('autoclicker')

def performance_monitor(func: Callable) -> Callable:
    """Decorator for tracking execution overhead of click actions."""
    @functools.lru_cache(maxsize=128)
    def cached_timer(f_name: str) -> str:
        return f"Execution speed logged for {f_name}"

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        
        # Only log excessive latency to reduce IO bottleneck
        if duration > 0.05:
            logger.warning(f"High latency detected in {func.__name__}: {duration:.4f}s")
        return result
    return wrapper

def batch_log(messages: list[str]) -> None:
    """Batch processing to reduce system call overhead."""
    if messages:
        logger.info(" | ".join(messages))