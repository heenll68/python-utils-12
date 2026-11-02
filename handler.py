import json
import os

def load_click_settings(filepath='settings.json'):
    """Loads autoclicker configuration from a local file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": -1}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_settings(data, filepath='settings.json'):
    """Persists autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_settings(settings):
    """Ensures configuration values are within safe ranges."""
    valid_buttons = ['left', 'right', 'middle']
    interval = settings.get('interval', 0.1)
    
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False
    
    if settings.get('button') not in valid_buttons:
        return False
        
    return True