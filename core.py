import time
import threading
from typing import Callable

class ClickEngine:
    """High-performance autoclicker engine using polling optimization."""

    def __init__(self, interval: float, callback: Callable):
        self.interval = interval
        self.callback = callback
        self._running = False
        self._thread = None

    def _run(self):
        """Executes click loop with minimal drift via delta timing."""
        next_click = time.perf_counter()
        while self._running:
            now = time.perf_counter()
            if now >= next_click:
                self.callback()
                next_click += self.interval
            else:
                # Sleep for remaining time to reduce CPU overhead
                sleep_time = max(0, next_click - now)
                time.sleep(sleep_time)

    def start(self):
        """Spawns click execution thread."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run, daemon=True)
            self._thread.start()

    def stop(self):
        """Signals thread termination."""
        self._running = False
        if self._thread:
            self._thread.join()
            self._thread = None