import time
import pyautogui
from typing import Optional

class ClickProcessor:
    """Handles click execution logic with interval management."""

    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def start(self) -> None:
        """Starts the click loop."""
        self.running = True
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

    def stop(self) -> None:
        """Terminates the click loop safely."""
        self.running = False

    def update_interval(self, new_interval: float) -> None:
        """Updates click frequency safely."""
        if new_interval > 0:
            self.interval = new_interval

    @staticmethod
    def get_mouse_position() -> tuple:
        """Retrieves current coordinates."""
        return pyautogui.position()