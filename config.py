import json
import os
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval": 0.1,
    "button": "left",
    "max_clicks": 1000,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists configuration to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    # Module usage for local configuration validation
    current_config = load_config()
    print(f"Active configuration loaded: {current_config}")