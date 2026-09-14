import json
import os
from typing import Dict, Any

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Reads click settings from a JSON configuration file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 0}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists current autoclicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Checks if click interval and repeats are valid."""
    interval = data.get("interval", 0)
    repeats = data.get("repeats", 0)
    return isinstance(interval, (int, float)) and interval >= 0 and isinstance(repeats, int)