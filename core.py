import ctypes
import time
import threading
from typing import Optional


class FastClickEngine:
    """High-precision autoclicker engine optimized for sub-millisecond accuracy."""

    def __init__(self, target_cps: float = 100.0) -> None:
        self.interval = 1.0 / max(target_cps, 0.1)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._click_count = 0

        # Pre-load win32 API calls to remove runtime lookup overhead
        try:
            self._mouse_event = ctypes.windll.user32.mouse_event
            self._has_win32 = True
        except (AttributeError, OSError):
            self._has_win32 = False

    def _raw_click(self) -> None:
        """Execute mouse down and up events directly."""
        if self._has_win32:
            # 0x0002: MOUSEEVENTF_LEFTDOWN, 0x0004: MOUSEEVENTF_LEFTUP
            self._mouse_event(0x0002, 0, 0, 0, 0)
            self._mouse_event(0x0004, 0, 0, 0, 0)
        self._click_count += 1

    def _run_loop(self) -> None:
        """Hybrid loop combining OS sleep and high-resolution spin-wait."""
        next_time = time.perf_counter()

        while self._running:
            now = time.perf_counter()
            if now >= next_time:
                self._raw_click()
                next_time = max(next_time + self.interval, time.perf_counter())
            else:
                remaining = next_time - now
                if remaining > 0.002:
                    time.sleep(remaining - 0.001)

    def start(self) -> None:
        """Start execution thread."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        """Stop execution thread safely."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    @property
    def total_clicks(self) -> int:
        return self._click_count
