import json
import os

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.load_config()

    def load_config(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = self.default_config()

    def default_config(self):
        return {
            'click_interval': 0.1,
            'click_count': 10,
            'click_button': 'left'
        }

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)

    def update_config(self, key, value):
        if key in self.config:
            self.config[key] = value
            self.save_config()
        else:
            raise KeyError(f'Config key {key} not found.')