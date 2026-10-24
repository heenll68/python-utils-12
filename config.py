import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(filepath: str) -> Dict[str, Any]:
    """
    Loads configuration from json file with fallback to defaults.
    Returns merged dictionary containing final settings.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> bool:
    """
    Persists provided configuration dictionary to specified json file.
    Returns True if operation succeeded.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False