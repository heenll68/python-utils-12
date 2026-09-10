import json
import os

class ConfigError(Exception):
    """Custom exception for configuration loading errors."""
    pass

def load_config(filepath):
    """Safely load JSON config with fallback to defaults."""
    defaults = {
        "interval": 0.1,
        "button": "left",
        "hotkey": "f6"
    }

    if not os.path.exists(filepath):
        return defaults

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
            # Validate required fields
            if not isinstance(data.get("interval"), (int, float)) or data["interval"] < 0:
                raise ConfigError("Invalid interval: must be non-negative number")
                
            return {**defaults, **data}
    except (json.JSONDecodeError, PermissionError, ConfigError) as e:
        print(f"Config error: {e}. Using default values.")
        return defaults

def save_config(filepath, config_data):
    """Atomic-like save attempt for user settings."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config_data, f, indent=4)
    except (IOError, TypeError) as e:
        print(f"Failed to write config: {e}")