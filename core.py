import time
import threading
from typing import Callable, Optional

class FastClicker:
    """High-performance autoclicker engine with micro-sleep timing optimization."""

    def __init__(self, click_func: Callable[[], None], interval: float = 0.001):
        self.click_func = click_func
        self.interval = max(0.0001, interval)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._click_count = 0

    def start(self) -> None:
        """Start the clicker in a dedicated background thread."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop the click loop cleanly."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        self._thread = None

    def _run_loop(self) -> None:
        """Optimized loop using hybrid sleep and spin-lock for high accuracy."""
        target_time = time.perf_counter()
        while self._running:
            self.click_func()
            self._click_count += 1
            target_time += self.interval

            # Yield CPU for larger delays, spin-lock for sub-millisecond precision
            sleep_duration = target_time - time.perf_counter()
            if sleep_duration > 0.002:
                time.sleep(sleep_duration - 0.001)

            while time.perf_counter() < target_time:
                pass

    @property
    def total_clicks(self) -> int:
        return self._click_count
