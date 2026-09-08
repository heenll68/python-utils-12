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
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge defaults with loaded config
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save config: {e}")

if __name__ == "__main__":
    current_cfg = load_config()
    print(f"Active configuration: {current_cfg}")