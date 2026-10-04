import time
import pyautogui
from typing import Optional

class AutoClicker:
    """Optimized clicker engine using reduced system calls."""
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._running = False
        pyautogui.PAUSE = 0

    def start(self, duration: Optional[int] = None) -> None:
        """Executes clicks using high-frequency loop optimization."""
        self._running = True
        start_time = time.perf_counter()
        
        try:
            while self._running:
                pyautogui.click()
                if self.interval > 0:
                    time.sleep(self.interval)
                
                if duration and (time.perf_counter() - start_time) > duration:
                    break
        except KeyboardInterrupt:
            self.stop()

    def stop(self) -> None:
        """Stops the execution loop immediately."""
        self._running = False

    def update_interval(self, new_interval: float) -> None:
        """Updates click frequency without restarting process."""
        self.interval = max(0.0, new_interval)