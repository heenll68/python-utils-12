import logging
import json
from datetime import datetime
from pathlib import Path

class ClickLogger:
    """Handles persistent storage of click event logs."""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_path = Path(log_dir)
        self.log_path.mkdir(exist_ok=True)
        self.file_path = self.log_path / "click_history.jsonl"
        
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger("autoclicker")

    def log_event(self, action: str, coordinates: tuple) -> None:
        """Appends a structured click event to the log file."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "x": coordinates[0],
            "y": coordinates[1]
        }
        
        try:
            with open(self.file_path, "a") as f:
                f.write(json.dumps(entry) + "\n")
            self.logger.info(f"Logged {action} at {coordinates}")
        except IOError as e:
            self.logger.error(f"Failed to write log: {e}")

    def get_recent_events(self, limit: int = 10) -> list:
        """Retrieves the most recent click events."""
        if not self.file_path.exists():
            return []
        
        with open(self.file_path, "r") as f:
            lines = f.readlines()
            return [json.loads(line) for line in lines[-limit:]]