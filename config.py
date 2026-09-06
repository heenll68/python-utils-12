import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 100,
    "hotkey": "f8"
}

CONFIG_FILE = "settings.json"

def load_config() -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure missing keys are handled
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to local storage."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

# Initialize configuration settings on module load
app_config = load_config()