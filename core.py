import time
import threading

try:
    from pynput.mouse import Button, Controller
except ImportError:
    # Fallback simulation for environments without pynput
    class Button:
        left = 'left'
        right = 'right'
    class Controller:
        def click(self, button):
            pass

class AutoClicker:
    """Thread-safe autoclicker engine with controlled delay."""
    def __init__(self, delay: float = 0.1, button = Button.left):
        self.delay = delay
        self.button = button
        self.running = False
        self.active = True
        self.mouse = Controller()
        self._thread = threading.Thread(target=self._click_loop, daemon=True)
        self._thread.start()

    def start_clicking(self):
        """Enable the click generation."""
        self.running = True

    def pause_clicking(self):
        """Temporarily halt click generation."""
        self.running = False

    def stop_clicking(self):
        """Permanently shut down the clicker thread."""
        self.running = False
        self.active = False

    def _click_loop(self):
        """Background loop execution for clicking."""
        while self.active:
            if self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            else:
                time.sleep(0.01)
