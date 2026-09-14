from typing import Final, Dict, Any

# Default click interval in seconds
DEFAULT_INTERVAL: Final[float] = 0.1

# Mouse button identifiers
LEFT_BUTTON: Final[str] = "left"
RIGHT_BUTTON: Final[str] = "right"
MIDDLE_BUTTON: Final[str] = "middle"

# Configuration key mappings
CONFIG_KEYS: Final[Dict[str, Any]] = {
    "interval": float,
    "button": str,
    "iterations": int,
    "toggle_key": str
}

# Max click rate limit to prevent system freezing
MAX_CLICK_RATE: Final[int] = 1000

# Error and status messages
STATUS_READY: Final[str] = "autoclicker system initialized"
STATUS_RUNNING: Final[str] = "click sequence active"
STATUS_STOPPED: Final[str] = "process terminated by user"

def get_default_config() -> Dict[str, Any]:
    """Returns the default configuration dictionary for the application."""
    return {
        "interval": DEFAULT_INTERVAL,
        "button": LEFT_BUTTON,
        "iterations": -1,
        "toggle_key": "f6"
    }