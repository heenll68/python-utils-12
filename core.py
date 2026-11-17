import time
import threading
from typing import Callable

class ClickEngine:
    """Optimized execution loop for high-frequency input simulation."""
    def __init__(self, interval: float, action: Callable):
        self.interval = interval
        self.action = action
        self._running = False
        self._thread = None

    def _run_loop(self):
        """Executes action with minimal latency overhead."""
        # Pre-cache interval for micro-optimization
        delta = self.interval
        last_time = time.perf_counter()

        while self._running:
            self.action()
            
            # Calculate precise sleep duration to combat drift
            elapsed = time.perf_counter() - last_time
            sleep_time = delta - elapsed
            
            if sleep_time > 0:
                time.sleep(sleep_time)
            
            last_time = time.perf_counter()

    def start(self):
        """Initiates processing thread with thread-safe toggle."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

    def stop(self):
        """Terminates the execution loop."""
        self._running = False
        if self._thread:
            self._thread.join()
            self._thread = None