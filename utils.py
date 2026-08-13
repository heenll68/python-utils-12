import time
import threading

class AutoClicker:
    def __init__(self, delay=1.0):
        self.is_running = False
        self.delay = delay
        self.click_thread = None

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.click_thread = threading.Thread(target=self._click)
            self.click_thread.start()

    def stop(self):
        self.is_running = False
        if self.click_thread is not None:
            self.click_thread.join()

    def _click(self):
        while self.is_running:
            self.perform_click()
            time.sleep(self.delay)

    @staticmethod
    def perform_click():
        print("Click!")  # Simulate a mouse click

if __name__ == '__main__':
    autoclicker = AutoClicker(delay=0.5)  # Adjust delay as needed
    autoclicker.start()
    time.sleep(5)  # Run for 5 seconds
    autoclicker.stop()