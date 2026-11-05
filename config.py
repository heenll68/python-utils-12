import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with fallback to defaults.
    If file is missing or invalid, initializes with standard values.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        _save_config(filepath, config)
        return config

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def _save_config(filepath: str, config: Dict[str, Any]) -> None:
    """
    Persists the provided configuration dictionary to the filesystem.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass