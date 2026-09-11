import time
import pyautogui
from typing import Tuple

class AutoClicker:
    """High-performance autoclicker engine core."""
    
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._running = False
        # Pre-bind function to reduce lookup overhead in loops
        self._click = pyautogui.click

    def set_interval(self, seconds: float):
        self.interval = max(0.001, seconds)

    def start(self):
        """Starts the click loop with performance optimizations."""
        self._running = True
        self._run_loop()

    def stop(self):
        self._running = False

    def _run_loop(self):
        """Core execution loop with local caching."""
        click_func = self._click
        sleep_func = time.sleep
        delay = self.interval
        
        # Local variables optimize loop performance by reducing attribute lookups
        while self._running:
            click_func()
            if delay > 0:
                sleep_func(delay)

if __name__ == '__main__':
    bot = AutoClicker(interval=0.05)
    try:
        bot.start()
    except KeyboardInterrupt:
        bot.stop()