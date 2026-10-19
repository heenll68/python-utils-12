import time
import pyautogui
from typing import Optional

class AutoClicker:
    """Core engine for automated mouse clicking operations."""

    def __init__(self, interval: float = 0.1, button: str = 'left'):
        self.interval = interval
        self.button = button
        self.is_running = False

    def start_clicking(self, duration: Optional[int] = None) -> None:
        """Executes clicks until duration expires or stopped."""
        self.is_running = True
        start_time = time.time()

        try:
            while self.is_running:
                if duration and (time.time() - start_time) > duration:
                    break
                
                pyautogui.click(button=self.button)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.stop_clicking()

    def stop_clicking(self) -> None:
        """Graceful termination of clicking sequence."""
        self.is_running = False

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    clicker.start_clicking(duration=10)