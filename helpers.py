import json
import os
from typing import Dict, Any

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker parameters from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "clicks": 1}

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"interval": 0.1, "button": "left", "clicks": 1}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(interval: float) -> float:
    """Ensures click interval is within safe bounds."""
    return max(0.01, min(interval, 60.0))

def format_click_payload(x: int, y: int, button: str) -> Dict[str, Any]:
    """Constructs structured data for click events."""
    return {
        "position": {"x": x, "y": y},
        "button": button.lower(),
        "timestamp": "placeholder"
    }