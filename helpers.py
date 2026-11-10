import json
import os
from typing import Dict, Any

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker parameters from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": -1}

    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Ensures configuration values are within safe bounds."""
    required_keys = {"interval", "button", "repeat"}
    if not required_keys.issubset(data.keys()):
        return False
    
    if not isinstance(data["interval"], (int, float)) or data["interval"] < 0.01:
        return False
    
    return data["button"] in ["left", "right", "middle"]
