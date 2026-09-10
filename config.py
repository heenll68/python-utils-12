import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hold_time": 0.05,
    "autostart": False,
    "log_level": "INFO"
}

CONFIG_FILE = "settings.json"

def load_config() -> Dict[str, Any]:
    """Loads configuration from JSON file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not read {CONFIG_FILE}, using defaults.")
    
    return config

def save_config(config: Dict[str, Any]) -> None:
    """Persists current configuration state to disk."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save configuration: {e}")