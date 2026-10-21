import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "clicks_per_second": 10.0,
    "mouse_button": "left",
    "click_type": "single",
    "hotkey": "f6",
    "random_jitter_ms": 15,
    "target_window": None,
    "max_clicks": 0,
}


class ConfigLoader:
    """Handles loading and saving autoclicker configuration with default fallback options."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Load configuration from disk, creating default file if missing."""
        if not os.path.exists(self.config_path):
            self.save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)

            config = DEFAULT_CONFIG.copy()
            if isinstance(user_config, dict):
                config.update(user_config)
            return config
        except (json.JSONDecodeError, OSError):
            return DEFAULT_CONFIG.copy()

    def save(self, config_data: Dict[str, Any]) -> bool:
        """Save configuration dictionary to JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4)
            return True
        except OSError:
            return False