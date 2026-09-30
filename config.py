import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # in seconds
    "mouse_button": "left",  # left, right, middle
    "hotkey_start_stop": "f8",
    "click_type": "single",  # single, double
    "random_delay_range": [0.0, 0.02],  # adds realism to clicking
}


class ConfigLoader:
    """Manages loading, validating, and saving autoclicker settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from disk or falls back to defaults."""
        if not os.path.exists(self.config_path):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Merge loaded data with defaults to handle missing keys
            merged = DEFAULT_CONFIG.copy()
            if isinstance(data, dict):
                merged.update(data)
            return merged
        except (json.JSONDecodeError, OSError):
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any]) -> None:
        """Saves the configuration dictionary back to the JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4)
        except OSError:
            pass

    def get(self, key: str) -> Any:
        """Retrieves a configuration option."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def update(self, key: str, value: Any) -> bool:
        """Updates a configuration setting if the key is valid."""
        if key in DEFAULT_CONFIG:
            self.config[key] = value
            self.save_config(self.config)
            return True
        return False
