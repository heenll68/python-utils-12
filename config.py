import json
import os

class ConfigError(Exception):
    """Custom exception for configuration loading issues."""
    pass

def load_config(filepath):
    """Loads and validates JSON configuration for the autoclicker."""
    if not os.path.exists(filepath):
        raise ConfigError(f"Configuration file not found: {filepath}")

    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise ConfigError(f"Malformed JSON in configuration: {e}")
    except PermissionError:
        raise ConfigError(f"Insufficient permissions to read: {filepath}")

    # Validate mandatory fields
    required_fields = ['click_interval', 'max_clicks']
    for field in required_fields:
        if field not in config:
            raise ConfigError(f"Missing required field: {field}")
        if not isinstance(config[field], (int, float)) or config[field] < 0:
            raise ConfigError(f"Invalid value for {field}: must be positive number")

    return config

def get_default_config():
    """Returns hardcoded safe defaults if file is missing."""
    return {
        "click_interval": 0.1,
        "max_clicks": 1000,
        "button": "left"
    }