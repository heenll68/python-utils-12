import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 100,
    "hotkey": "f8"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON or return defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Failed to read {config_path}, using defaults.")
    
    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persist current configuration to disk."""
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error saving config: {e}")