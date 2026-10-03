import time
import pyautogui
from typing import Dict, Any, Optional

class ClickHandler:
    """Handles automated click execution with safety delays."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize handler with a base click interval."""
        self.interval: float = interval

    def perform_click(self, x: int, y: int, button: str = "left") -> None:
        """Executes a mouse click at the specified coordinates."""
        pyautogui.click(x=x, y=y, button=button)
        time.sleep(self.interval)

    def perform_sequence(self, coordinates: list[tuple[int, int]]) -> None:
        """Executes a series of clicks in order."""
        for x, y in coordinates:
            self.perform_click(x, y)

    def get_status(self) -> Dict[str, Any]:
        """Retrieves the current operational status of the handler."""
        return {
            "interval": self.interval,
            "active": True,
            "platform": "pyautogui"
        }

    def safe_stop(self, delay: float = 0.5) -> None:
        """Forces a pause to prevent runaway click sequences."""
        time.sleep(delay)