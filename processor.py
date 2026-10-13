import time
import threading
from queue import Queue

class ClickProcessor:
    def __init__(self, interval_ms=10):
        self.queue = Queue(maxsize=100)
        self.interval = interval_ms / 1000.0
        self.running = True

    def submit_click(self, x: int, y: int):
        """Non-blocking submission of click coordinates."""
        if not self.queue.full():
            self.queue.put((x, y))

    def _process_loop(self):
        """Optimized execution loop using time.perf_counter."""
        last_time = time.perf_counter()
        while self.running:
            current_time = time.perf_counter()
            if current_time - last_time >= self.interval:
                if not self.queue.empty():
                    x, y = self.queue.get()
                    self._execute_native_click(x, y)
                    last_time = current_time
            time.sleep(0.001)

    def _execute_native_click(self, x, y):
        """Hardware-level click abstraction placeholder."""
        pass

    def start(self):
        self.thread = threading.Thread(target=self._process_loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()