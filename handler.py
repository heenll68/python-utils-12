import time
import pyautogui
from typing import Optional

class ClickHandler:
    """Handles click operations and event timing."""
    
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def start_clicking(self) -> None:
        """Initiates the main clicking sequence."""
        self.running = True
        try:
            while self.running:
                pyautogui.click()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.stop_clicking()

    def stop_clicking(self) -> None:
        """Gracefully halts the click loop."""
        self.running = False

    def set_interval(self, new_interval: float) -> None:
        """Updates the click delay duration."""
        if new_interval > 0:
            self.interval = new_interval

if __name__ == "__main__":
    handler = ClickHandler(interval=0.5)
    print("Starting autoclicker (Ctrl+C to stop)...")
    handler.start_clicking()