import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(filepath: str) -> dict:
    """Loads configuration from json file or returns defaults."""
    if not os.path.exists(filepath):
        save_config(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(filepath: str, config: dict) -> None:
    """Saves current configuration state to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

if __name__ == "__main__":
    # Example usage
    cfg = load_config("config.json")
    print(f"Loaded interval: {cfg['interval']}")