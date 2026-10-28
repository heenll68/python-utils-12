import time
import logging
from typing import Tuple, Optional, Callable

logger = logging.getLogger(__name__)


class ClickProcessor:
    """Processes click events with boundary safety and error handling."""

    def __init__(self, screen_bounds: Tuple[int, int] = (1920, 1080), max_cps: float = 100.0):
        self.screen_bounds = screen_bounds
        self.max_cps = max_cps
        self.failsafe_triggered = False

    def validate_coordinates(self, x: int, y: int) -> bool:
        """Check if click target coordinates stay within safe screen bounds."""
        max_x, max_y = self.screen_bounds
        if x < 0 or y < 0 or x > max_x or y > max_y:
            logger.warning(f"Target coordinates ({x}, {y}) out of screen bounds {self.screen_bounds}")
            return False
        return True

    def execute_click(self, x: int, y: int, interval: float, click_func: Optional[Callable[[int, int], None]] = None) -> bool:
        """Safely run click action while handling invalid inputs and unexpected errors."""
        if self.failsafe_triggered:
            logger.error("Click execution aborted: Failsafe state active")
            return False

        if not self.validate_coordinates(x, y):
            return False

        # Clamp unsafe click intervals to prevent infinite or CPU-hogging loops
        if interval <= 0 or (1.0 / interval) > self.max_cps:
            safe_interval = max(1.0 / self.max_cps, 0.001)
            logger.warning(f"Invalid interval {interval}s; corrected to {safe_interval}s")
            interval = safe_interval

        try:
            if click_func:
                click_func(x, y)
            time.sleep(interval)
            return True
        except (PermissionError, OSError) as e:
            logger.error(f"OS hardware input error at ({x}, {y}): {e}")
            return False
        except Exception as e:
            logger.critical(f"Unhandled error during click dispatch: {e}")
            self.failsafe_triggered = True
            return False
