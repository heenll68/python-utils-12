import time
import threading
from typing import Callable, Optional

class ClickOptimizer:
    """High-performance click execution handler using pre-compiled loops."""
    
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def _execute(self, action: Callable, iterations: int):
        """Internal loop using local variable caching for speed."""
        interval = self.interval
        while self._running and iterations > 0:
            action()
            time.sleep(interval)
            iterations -= 1

    def start(self, action: Callable, iterations: int = 1000):
        """Spawns worker thread for non-blocking execution."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(
                target=self._execute, 
                args=(action, iterations),
                daemon=True
            )
            self._thread.start()

    def stop(self):
        """Signals thread termination and cleans up resources."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)
            self._thread = None