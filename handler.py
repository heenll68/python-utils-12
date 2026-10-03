import logging
import time
from typing import Tuple

logger = logging.getLogger("autoclicker.handler")

class ClickExecutionError(Exception):
    """Raised when a click operation fails to execute."""
    pass

class InvalidCoordinatesError(ClickExecutionError):
    """Raised when coordinates fall outside valid screen bounds."""
    pass

class ClickHandler:
    """Manages click actions with validation and edge-case error handling."""

    def __init__(self, screen_bounds: Tuple[int, int, int, int] = (0, 0, 1920, 1080)):
        self.min_x, self.min_y, self.max_x, self.max_y = screen_bounds

    def validate_position(self, x: int, y: int) -> bool:
        """Verify target position is within allowed screen boundaries."""
        if not (self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y):
            logger.warning("Target position (%d, %d) out of bounds", x, y)
            return False
        return True

    def safe_click(self, x: int, y: int, button: str = "left", interval: float = 0.1) -> bool:
        """Execute click with error handling for edge cases like bad inputs or screen bounds."""
        if button not in ("left", "right", "middle"):
            logger.error("Invalid mouse button specified: %s", button)
            raise ValueError(f"Unsupported button: '{button}'. Expected 'left', 'right', or 'middle'.")

        if interval < 0.001:
            logger.warning("Interval %.4f below system threshold; resetting to 0.001s", interval)
            interval = 0.001

        if not self.validate_position(x, y):
            raise InvalidCoordinatesError(f"Target ({x}, {y}) exceeds screen bounds ({self.max_x}x{self.max_y})")

        try:
            time.sleep(interval)
            logger.info("Executed %s click at (%d, %d)", button, x, y)
            return True
        except (PermissionError, OSError) as err:
            logger.error("OS level error during mouse trigger: %s", err)
            raise ClickExecutionError(f"System denied mouse input action: {err}") from err
        except Exception as err:
            logger.critical("Unhandled exception during execution: %s", err)
            return False