AUTOCLICKER_SPEED = 0.1  # Time in seconds between clicks
AUTOCLICKER_DEFAULT_COUNT = 100  # Default number of clicks
AUTOCLICKER_MAX_CLICKS = 10000  # Maximum allowed clicks
CLICK_BUTTON = "left"  # Default click button (left/right)
AUTOCLICKER_MODE = "single"  # Modes: single or continuous

# Define possible click modes
CLICK_MODES = {
    "single": "Single click once",
    "continuous": "Hold down for continuous clicking"
}

# Hotkey settings
HOTKEYS = {
    "start_stop": "ctrl+shift+s",  # Hotkey to start/stop clicking
    "exit": "ctrl+shift+e"  # Hotkey to exit the application
}

# Error messages
ERROR_MESSAGES = {
    "invalid_mode": "Invalid click mode selected.",
    "input_out_of_bounds": "Input value is out of allowed range."
}

# General settings
DEBUG_MODE = False  # Enable or disable debug information
LOG_FILE = "autoclicker.log"  # Log file location
