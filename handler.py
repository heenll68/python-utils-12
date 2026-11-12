import time
from typing import Callable, Optional, Tuple


class ClickHandler:
    """Handles screen clicking operations based on target coordinates and frequency."""

    def __init__(self, click_func: Callable[[int, int], None]) -> None:
        """Initialize the ClickHandler with a mouse click execution function.

        Args:
            click_func: Callable that accepts (x, y) coordinates to trigger a click.
        """
        self._click_func: Callable[[int, int], None] = click_func
        self.total_clicks: int = 0
        self.is_running: bool = False

    def execute_single_click(self, target: Tuple[int, int]) -> bool:
        """Execute a single mouse click at the specified target coordinates.

        Args:
            target: A tuple containing (x, y) screen pixel coordinates.

        Returns:
            True if the click was dispatched successfully, False otherwise.
        """
        x, y = target
        if x < 0 or y < 0:
            return False

        self._click_func(x, y)
        self.total_clicks += 1
        return True

    def run_click_burst(
        self,
        target: Tuple[int, int],
        count: int,
        interval_seconds: float = 0.1,
    ) -> int:
        """Perform a rapid sequence of clicks at a given target location.

        Args:
            target: Tuple of (x, y) pixel coordinates.
            count: Total number of clicks to attempt.
            interval_seconds: Delay between clicks in seconds.

        Returns:
            Total count of successful clicks executed in the burst.
        """
        self.is_running = True
        successful_clicks: int = 0

        for _ in range(count):
            if not self.is_running:
                break
            if self.execute_single_click(target):
                successful_clicks += 1
            time.sleep(max(0.0, interval_seconds))

        self.is_running = False
        return successful_clicks

    def stop(self) -> None:
        """Stop any active click sequence immediately."""
        self.is_running = False
