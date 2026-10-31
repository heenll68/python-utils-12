import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # Delay between clicks in seconds
    "click_button": "left",  # Options: 'left', 'right', 'middle'
    "toggle_hotkey": "f6",  # Key to start/stop clicking
    "random_jitter": 0.01,  # Random delay offset for human-like behavior
    "max_clicks": 0,  # 0 indicates infinite clicking
    "start_delay": 0.0,  # Countdown before starting
}


def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file, merging user options with defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                user_data = json.load(file)
                if isinstance(user_data, dict):
                    for key, value in user_data.items():
                        if key in DEFAULT_CONFIG and isinstance(
                            value, type(DEFAULT_CONFIG[key])
                        ):
                            config[key] = value
        except (json.JSONDecodeError, OSError):
            pass

    return config


def save_config(config: Dict[str, Any], filepath: str = "config.json") -> bool:
    """Save active configuration settings to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
        return True
    except OSError:
        return False
