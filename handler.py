import json
import os
from typing import Dict, Any

def load_clicker_profile(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "enabled": False}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"interval": 0.1, "button": "left", "enabled": False}

def save_clicker_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to disk safely."""
    try:
        temp_path = f"{filepath}.tmp"
        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(temp_path, filepath)
        return True
    except (IOError, TypeError):
        return False

def validate_profile(data: Dict[str, Any]) -> bool:
    """Ensures configuration values are within safe bounds."""
    interval = data.get("interval", 0.1)
    button = data.get("button", "left")
    
    valid_interval = isinstance(interval, (int, float)) and interval > 0.001
    valid_button = button in ["left", "right", "middle"]
    
    return valid_interval and valid_button