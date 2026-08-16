import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval  # Time between clicks in seconds
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.start()

    def stop(self):
        self.running = False
        if hasattr(self, 'click_thread'):
            self.click_thread.join()  # Wait for the thread to finish

    def _click_loop(self):
        while self.running:
            self.perform_click()
            time.sleep(self.interval)  # Wait for the specified interval

    def perform_click(self):
        # Simulates a mouse click action (to be implemented)
        print('Click!')  # Placeholder for actual click action

if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.5)  # Create an instance with a 0.5s interval
    autoclicker.start()  # Start the autoclicker
    time.sleep(5)  # Let it click for 5 seconds
    autoclicker.stop()  # Stop the autoclicker