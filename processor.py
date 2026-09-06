import json
import os
from typing import Dict, Any

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to a local JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Storage error: {e}")
        return False

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker settings from a specified path."""
    if not os.path.exists(filepath):
        return {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def validate_interval(interval: float) -> float:
    """Ensures click interval remains within logical bounds."""
    return max(0.01, min(interval, 60.0))

def format_coords(x: int, y: int) -> Dict[str, int]:
    """Encapsulates coordinate data for clicker input."""
    return {"x": int(x), "y": int(y)}
