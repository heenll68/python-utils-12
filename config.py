import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval": 0.1,
    "button": "left",
    "click_type": "single",
    "target_location": None,
    "max_clicks": 0,
}

VALID_BUTTONS = {"left", "right", "middle"}
VALID_TYPES = {"single", "double"}


class ConfigError(Exception):
    """Custom exception raised for invalid autoclicker configuration."""
    pass


class AutoclickerConfig:
    """Manages and validates configuration settings with edge-case handling."""

    def __init__(self, filepath: str = "config.json") -> None:
        self.filepath = filepath
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads config file, handling missing or corrupted files gracefully."""
        if not os.path.exists(self.filepath):
            self.save()
            return self.config

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.config.update(data)
        except (json.JSONDecodeError, PermissionError, OSError):
            # Fallback to defaults on corrupted file or read failure
            self.config = DEFAULT_CONFIG.copy()

        self.sanitize()
        return self.config

    def sanitize(self) -> None:
        """Sanitizes configuration values and handles invalid or out-of-bounds parameters."""
        # Sanitize click interval
        try:
            interval = float(self.config.get("interval", 0.1))
            self.config["interval"] = max(0.001, interval)
        except (ValueError, TypeError):
            self.config["interval"] = 0.1

        # Sanitize click button
        if self.config.get("button") not in VALID_BUTTONS:
            self.config["button"] = "left"

        # Sanitize click type
        if self.config.get("click_type") not in VALID_TYPES:
            self.config["click_type"] = "single"

        # Sanitize coordinate edge cases (negative or invalid tuple)
        loc = self.config.get("target_location")
        if loc is not None:
            if not isinstance(loc, (list, tuple)) or len(loc) != 2:
                self.config["target_location"] = None
            elif not all(isinstance(val, int) and val >= 0 for val in loc):
                self.config["target_location"] = None

    def save(self) -> bool:
        """Saves current validated configuration to file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            return True
        except OSError:
            return False
