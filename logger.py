import json
import os
from datetime import datetime

class ClickLogger:
    """Handles persistent storage of click event sequences."""
    def __init__(self, log_file: str = "click_data.json"):
        self.log_file = log_file

    def save_event(self, x: int, y: int, button: str):
        """Appends a click event to the log file."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "x": x,
            "y": y,
            "button": button
        }
        
        data = self._load_existing()
        data.append(entry)
        
        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=4)

    def _load_existing(self) -> list:
        """Reads current log data from disk."""
        if not os.path.exists(self.log_file):
            return []
        try:
            with open(self.log_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def clear_logs(self):
        """Deletes the log file if it exists."""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)