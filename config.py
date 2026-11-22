import os
import json
import logging

# Default configuration settings
DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": -1
}

def load_config(filepath: str) -> dict:
    """Load configuration from a JSON file with validation."""
    if not os.path.exists(filepath):
        logging.warning(f"Config file {filepath} not found, using defaults")
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Ensure required types for core autoclicker logic
            if not isinstance(data.get("interval", 0.1), (int, float)):
                raise ValueError("Interval must be a numeric value")
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, ValueError, PermissionError) as e:
        logging.error(f"Failed to load config: {e}. Falling back to defaults")
        return DEFAULT_CONFIG

def save_config(filepath: str, config: dict) -> bool:
    """Persist configuration to disk with error safety."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        logging.error(f"Configuration save failure: {e}")
        return False