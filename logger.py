import logging
import json
from datetime import datetime
from pathlib import Path

# Configure autoclicker event logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('autoclicker')

LOG_FILE = Path('click_history.json')

def log_click_event(coords: tuple, button: str, timestamp: float = None):
    """Records click action to local persistent storage."""
    data = {
        'x': coords[0],
        'y': coords[1],
        'button': button,
        'time': timestamp or datetime.now().timestamp()
    }

    try:
        history = []
        if LOG_FILE.exists():
            with open(LOG_FILE, 'r') as f:
                history = json.load(f)
        
        history.append(data)
        
        with open(LOG_FILE, 'w') as f:
            json.dump(history, f, indent=4)
            
        logger.info(f"Logged click at {coords}")
    except (IOError, json.JSONDecodeError) as e:
        logger.error(f"Failed to write click log: {e}")

def get_recent_clicks(limit: int = 10):
    """Retrieves the last N recorded click events."""
    if not LOG_FILE.exists():
        return []
    try:
        with open(LOG_FILE, 'r') as f:
            data = json.load(f)
            return data[-limit:]
    except Exception as e:
        logger.error(f"Error reading log file: {e}")
        return []