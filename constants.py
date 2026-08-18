MAX_CLICKS = 1000
MIN_CLICKS = 1
DEFAULT_DELAY = 0.1
CLICK_BUTTON = 'left'
CLICK_PATTERN = {'type': CLICK_BUTTON, 'count': MAX_CLICKS}

# Error messages
ERROR_NO_CLICKS = 'At least one click must be specified'
ERROR_DELAY_TOO_SHORT = 'Delay must be greater than zero'

# Settings
DEFAULT_SETTINGS = {
    'clicks': 100,
    'delay': DEFAULT_DELAY,
    'button': CLICK_BUTTON
}

# Configuration bounds
DELAY_BOUNDS = (0.01, 5.0)

# Operating system
IS_WINDOWS = True if os.name == 'nt' else False
IS_MAC = True if os.uname().sysname == 'Darwin' else False
IS_LINUX = True if os.name == 'posix' and not IS_MAC else False

# Click pattern
CLICK_PATTERN = {
    'button': CLICK_BUTTON,
    'delay_range': DELAY_BOUNDS
}
