import time
import threading
import pyautogui

class ClickProcessor:
    """Handles automated clicking sequences with thread safety."""

    def __init__(self, interval: float = 0.1, button: str = 'left'):
        self.interval = interval
        self.button = button
        self.active = False
        self._lock = threading.Lock()

    def start(self):
        """Starts the clicker thread if not already running."""
        with self._lock:
            if not self.active:
                self.active = True
                threading.Thread(target=self._run, daemon=True).start()

    def stop(self):
        """Signals the clicker thread to terminate."""
        with self._lock:
            self.active = False

    def _run(self):
        """Internal loop for continuous mouse clicks."""
        while True:
            with self._lock:
                if not self.active:
                    break
            
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def update_settings(self, interval: float, button: str):
        """Updates click timing and mouse button preference."""
        with self._lock:
            self.interval = interval
            self.button = button