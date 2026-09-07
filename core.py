import time
import pyautogui
from typing import Tuple

class AutoClicker:
    """Handles automated clicking sequences with configurable timing."""
    
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def start_clicking(self, iterations: int = 0) -> None:
        """Executes clicks until stopped or iteration limit met."""
        self.running = True
        count = 0
        try:
            while self.running:
                pyautogui.click()
                time.sleep(self.interval)
                count += 1
                if iterations > 0 and count >= iterations:
                    break
        except KeyboardInterrupt:
            self.stop_clicking()

    def stop_clicking(self) -> None:
        """Halts current click execution."""
        self.running = False

    def set_interval(self, seconds: float) -> None:
        """Updates click frequency."""
        self.interval = max(0.01, seconds)

def get_mouse_position() -> Tuple[int, int]:
    """Returns current screen coordinates."""
    return pyautogui.position()

if __name__ == "__main__":
    clicker = AutoClicker(interval=0.5)
    clicker.start_clicking(iterations=5)