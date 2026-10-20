import platform

# Operating system identification
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# Mouse button identifiers for automation
MOUSE_LEFT = "left"
MOUSE_RIGHT = "right"
MOUSE_MIDDLE = "middle"

# Standard time delays in seconds
MIN_INTERVAL = 0.01
DEFAULT_INTERVAL = 0.1
MAX_INTERVAL = 60.0

# Configuration defaults
DEFAULT_CLICK_COUNT = 1
DEFAULT_KEY_BIND = "f8"

# Status codes for the main loop
STATUS_IDLE = 0
STATUS_RUNNING = 1
STATUS_PAUSED = 2
STATUS_STOPPED = 3

# Key event types
EVENT_PRESS = "press"
EVENT_RELEASE = "release"

# Coordinates validation boundaries
MIN_SCREEN_X = 0
MIN_SCREEN_Y = 0
MAX_SCREEN_X = 10000
MAX_SCREEN_Y = 10000

def get_app_title():
    """Return the project name identifier."""
    return "python-utils-12-autoclicker"