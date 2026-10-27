import platform

# Operating system identification
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# Standard button identifiers for input simulation
LEFT_BUTTON = "left"
RIGHT_BUTTON = "right"
MIDDLE_BUTTON = "middle"

# Default operation constraints
DEFAULT_CLICK_INTERVAL = 0.1
MAX_CLICK_INTERVAL = 60.0
MIN_CLICK_INTERVAL = 0.001

# Key constants for hotkey registration
KEY_START_STOP = "f6"
KEY_EXIT = "f7"

# GUI configuration placeholders
DEFAULT_WINDOW_TITLE = "Python Utils 12 - Autoclicker"
DEFAULT_WINDOW_SIZE = "300x200"

# Valid button choices for dropdown selections
VALID_BUTTONS = [LEFT_BUTTON, RIGHT_BUTTON, MIDDLE_BUTTON]

# Configuration file path
CONFIG_FILE_PATH = "settings.json"

# Logging format constants
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"