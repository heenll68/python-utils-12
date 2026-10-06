import json
import os
from typing import Any, Dict

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker parameters from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "clicks": 1}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures screen coordinates are non-negative."""
    return x >= 0 and y >= 0

def format_click_stats(count: int, duration: float) -> str:
    """Generates a string representation of click session."""
    cps = count / duration if duration > 0 else 0
    return f"Total clicks: {count} | CPS: {cps:.2f}"