import json

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error loading config: {e}')
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.settings, file, indent=4)

# Example usage:
# config = Config('config.json')
# print(config.get('setting_name', 'default_value'))
# config.set('setting_name', 'new_value')