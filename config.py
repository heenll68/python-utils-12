import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cps": 10.0,
    "button": "left",
    "hotkey": "f6",
    "click_type": "single",
    "random_interval": True,
    "interval_jitter": 0.02,
    "max_clicks": 0,
    "sound_feedback": False,
}

class ConfigLoader:
    """Handles loading, saving, and managing autoclicker settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads config from JSON file or creates defaults if missing."""
        if not os.path.exists(self.config_path):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
            
            # Merge defaults for any missing keys
            config = DEFAULT_CONFIG.copy()
            config.update(loaded_data)
            return config
        except (json.JSONDecodeError, OSError):
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any]) -> bool:
        """Saves current configuration to the JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4)
            return True
        except OSError:
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a specific configuration setting."""
        return self.config.get(key, default)
