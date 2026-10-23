import time
import threading
from typing import Callable

class ClickHandler:
    """Handles click execution with jitter and batch processing."""

    def __init__(self, click_func: Callable[[], None], interval: float = 0.01):
        self.click_func = click_func
        self.interval = interval
        self._running = False
        self._thread = None

    def _run_loop(self):
        """Executes clicks using high-resolution timing."""
        next_call = time.perf_counter()
        while self._running:
            self.click_func()
            next_call += self.interval
            sleep_time = next_call - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                next_call = time.perf_counter()

    def start(self):
        """Spawns worker thread for click operations."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

    def stop(self):
        """Gracefully halts click execution."""
        self._running = False
        if self._thread:
            self._thread.join()