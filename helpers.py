import time
import threading
from typing import Callable, Any

def run_in_thread(target: Callable[..., Any], *args: Any, **kwargs: Any) -> threading.Thread:
    """
    Spawns a daemon thread for background tasks like autoclicking.

    :param target: Function to execute
    :param args: Positional arguments for the function
    :param kwargs: Keyword arguments for the function
    :return: The started thread object
    """
    thread = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True)
    thread.start()
    return thread

def sleep_ms(milliseconds: int) -> None:
    """
    Pause execution for a specific duration in milliseconds.

    :param milliseconds: Time to sleep in ms
    """
    time.sleep(milliseconds / 1000.0)

def format_interval(interval: float) -> str:
    """
    Converts interval float to a human-readable string representation.

    :param interval: Interval value in seconds
    :return: Formatted string
    """
    return f"{interval:.3f}s"