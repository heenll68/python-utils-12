from typing import Final

# Timing constraints for click intervals
MIN_INTERVAL: Final[float] = 0.01
MAX_INTERVAL: Final[float] = 60.0
DEFAULT_INTERVAL: Final[float] = 0.1

# Keyboard and mouse constants
CLICK_BUTTON_LEFT: Final[str] = "left"
CLICK_BUTTON_RIGHT: Final[str] = "right"
CLICK_BUTTON_MIDDLE: Final[str] = "middle"

# Application state defaults
DEFAULT_STOP_KEY: Final[str] = "f8"
MAX_CLICK_LIMIT: Final[int] = 1_000_000

# UI layout dimensions
WINDOW_WIDTH: Final[int] = 400
WINDOW_HEIGHT: Final[int] = 300

def get_valid_buttons() -> list[str]:
    """Returns the list of supported mouse button strings."""
    return [CLICK_BUTTON_LEFT, CLICK_BUTTON_RIGHT, CLICK_BUTTON_MIDDLE]