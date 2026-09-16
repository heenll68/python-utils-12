import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "randomize_timing": False
}

def load_config(filepath="config.json"):
    """Loads configuration from file with fallback to defaults."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config, filepath="config.json"):
    """Persists configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

if __name__ == "__main__":
    config = load_config()
    print(f"Loaded configuration: {config}")