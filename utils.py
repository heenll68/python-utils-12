import json
import os
from typing import Dict, Any

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker parameters from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 1}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"interval": 0.1, "button": "left", "repeats": 1}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_params(params: Dict[str, Any]) -> bool:
    """Verifies schema and ranges for click data."""
    required = {"interval", "button", "repeats"}
    if not all(key in params for key in required):
        return False
    
    if not isinstance(params["interval"], (int, float)) or params["interval"] < 0.001:
        return False
        
    if params["button"] not in ["left", "right", "middle"]:
        return False
        
    if not isinstance(params["repeats"], int) or params["repeats"] < 0:
        return False
        
    return True