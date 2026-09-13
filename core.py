import time
import threading
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class ClickConfig:
    interval: float = 0.1
    button: str = "left"
    max_clicks: int = 0


class AutoClicker:
    """Core engine managing automated clicking loop in a background thread."""

    def __init__(self, config: Optional[ClickConfig] = None) -> None:
        self.config = config or ClickConfig()
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self.click_count = 0

    def _click_loop(self, click_func: Callable[[], None]) -> None:
        while self._running:
            click_func()
            self.click_count += 1
            if 0 < self.config.max_clicks <= self.click_count:
                self._running = False
                break
            time.sleep(self.config.interval)

    def start(self, click_func: Callable[[], None]) -> None:
        """Start the autoclicker execution thread."""
        if self._running:
            return
        self._running = True
        self.click_count = 0
        self._thread = threading.Thread(
            target=self._click_loop, args=(click_func,), daemon=True
        )
        self._thread.start()

    def stop(self) -> None:
        """Stop the autoclicker and wait for thread termination."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
