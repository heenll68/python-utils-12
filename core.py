import time
import pyautogui
from typing import Tuple, Optional

class AutoClicker:
    """Handles periodic mouse clicking functionality."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize clicker with click frequency in seconds."""
        self.interval: float = interval
        self.is_running: bool = False

    def click(self, position: Optional[Tuple[int, int]] = None) -> None:
        """Perform a mouse click at a specific or current coordinate."""
        if position:
            pyautogui.click(x=position[0], y=position[1])
        else:
            pyautogui.click()

    def start_loop(self, duration: int, position: Optional[Tuple[int, int]] = None) -> None:
        """Execute clicks for a set duration."""
        self.is_running = True
        end_time = time.time() + duration
        
        while self.is_running and time.time() < end_time:
            self.click(position)
            time.sleep(self.interval)
        
        self.is_running = False

    def stop(self) -> None:
        """Terminate the active click loop."""
        self.is_running = False

if __name__ == "__main__":
    clicker = AutoClicker(interval=0.5)
    clicker.start_loop(duration=5)