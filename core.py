import ctypes
import sys
import time
from typing import Callable, Optional

class ClickEngine:
    """High-precision click execution engine optimized for low latency and minimal CPU drift."""

    def __init__(self, interval: float = 0.01) -> None:
        self.interval = max(0.0001, interval)
        self._is_running = False
        self._setup_precision_timer()

    def _setup_precision_timer(self) -> None:
        """Enable high-resolution timer on Windows to reduce sleep latency drift."""
        if sys.platform == "win32":
            try:
                ctypes.windll.winmm.timeBeginPeriod(1)
            except Exception:
                pass

    def _cleanup_precision_timer(self) -> None:
        """Restore default system timer resolution on Windows."""
        if sys.platform == "win32":
            try:
                ctypes.windll.winmm.timeEndPeriod(1)
            except Exception:
                pass

    def run(self, click_func: Callable[[], None], max_clicks: Optional[int] = None) -> int:
        """Executes click function with tight timing synchronization."""
        self._is_running = True
        total_clicks = 0
        next_tick = time.perf_counter()

        try:
            while self._is_running:
                if max_clicks is not None and total_clicks >= max_clicks:
                    break

                click_func()
                total_clicks += 1

                next_tick += self.interval
                sleep_time = next_tick - time.perf_counter()

                if sleep_time > 0:
                    time.sleep(sleep_time)
                else:
                    # Resynchronize next_tick if loop fell behind to avoid burst catch-up
                    next_tick = time.perf_counter()
        finally:
            self._is_running = False
            self._cleanup_precision_timer()

        return total_clicks

    def stop(self) -> None:
        """Signals execution loop to terminate gracefully."""
        self._is_running = False