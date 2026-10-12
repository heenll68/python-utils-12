import time
import threading
from pynput.mouse import Button, Controller

class AutoClicker:
    def __init__(self, interval: float = 0.01):
        self.mouse = Controller()
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start(self):
        with self._lock:
            self.running = True
        threading.Thread(target=self._run_loop, daemon=True).start()

    def stop(self):
        with self._lock:
            self.running = False

    def _run_loop(self):
        """High-frequency click loop with minimal overhead"""
        click_func = self.mouse.click
        btn = Button.left
        
        while True:
            with self._lock:
                if not self.running:
                    break
            
            click_func(btn)
            # Use sleep for lower CPU usage than busy-wait
            time.sleep(self.interval)

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.05)
    clicker.start()
    time.sleep(2)
    clicker.stop()