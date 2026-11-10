import time
import pyautogui
from typing import Optional

class AutoClicker:
    """Automates mouse clicks at defined intervals."""

    def __init__(self, interval: float = 1.0, button: str = 'left') -> None:
        """Initialize the clicker with delay and button configuration."""
        self.interval: float = interval
        self.button: str = button
        self._running: bool = False

    def start(self, duration: Optional[float] = None) -> None:
        """Begin the clicking loop for a specific duration."""
        self._running = True
        start_time: float = time.time()

        while self._running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

            if duration and (time.time() - start_time) >= duration:
                break

    def stop(self) -> None:
        """Halt the clicking loop."""
        self._running = False

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    try:
        clicker.start(duration=5.0)
    except KeyboardInterrupt:
        clicker.stop()