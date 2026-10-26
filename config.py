import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "double_click": False,
    "hotkey": "f6",
    "max_clicks": 0,
    "randomize_interval": True,
    "interval_jitter": 0.02,
}


def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file, merging user options with defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        save_config(filepath, config)
        return config

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            user_config = json.load(file)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, OSError):
        pass

    return config


def save_config(filepath: str, config: Dict[str, Any]) -> bool:
    """Save current configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
        return True
    except OSError:
        return False
