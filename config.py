import os
from typing import Dict, Any

class Config:
    """Configuration management for the autoclicker application."""
    def __init__(self, config_file: str) -> None:
        """Initialize theConfig object by loading settings from a config file."""
        self.config_file = config_file
        self.settings: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        """Load configuration settings from the specified file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        with open(self.config_file, 'r') as file:
            for line in file:
                key, value = line.strip().split('=', 1)
                self.settings[key] = self.cast_value(value)

    def cast_value(self, value: str) -> Any:
        """Cast a configuration value to the appropriate type."""
        if value.isdigit():
            return int(value)
        elif value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        return value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key, returning default if the key is not found."""
        return self.settings.get(key, default)
