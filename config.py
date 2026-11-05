import json
import os

class Config:
    """Manages autoclicker runtime settings."""
    DEFAULTS = {
        "interval": 0.1,
        "button": "left",
        "hotkey": "f8",
        "max_clicks": 0
    }

    def __init__(self, config_path="config.json"):
        self.path = config_path
        self.settings = self.load()

    def load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    return {**self.DEFAULTS, **json.load(f)}
            except (json.JSONDecodeError, IOError):
                pass
        return self.DEFAULTS.copy()

    def save(self):
        try:
            with open(self.path, "w") as f:
                json.dump(self.settings, f, indent=4)
        except IOError as e:
            print(f"Configuration save failure: {e}")

    def get(self, key):
        return self.settings.get(key, self.DEFAULTS.get(key))