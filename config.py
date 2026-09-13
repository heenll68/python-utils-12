import os

class Config:
    """Centralized configuration management for autoclicker"""
    
    DEFAULT_INTERVAL = 0.1
    DEFAULT_BUTTON = 'left'
    CONFIG_FILE = 'settings.json'

    def __init__(self):
        self.interval = float(os.getenv('CLICK_INTERVAL', self.DEFAULT_INTERVAL))
        self.button = os.getenv('CLICK_BUTTON', self.DEFAULT_BUTTON)
        self.is_running = False

    def update_settings(self, new_interval: float, new_button: str):
        """Update runtime click configuration"""
        if new_interval > 0:
            self.interval = new_interval
        if new_button in ['left', 'right', 'middle']:
            self.button = new_button

    def __repr__(self):
        return f"Config(interval={self.interval}, button='{self.button}')"

# Global config instance for easy access across modules
app_config = Config()