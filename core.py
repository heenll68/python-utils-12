import time
import threading
from dataclasses import dataclass

@dataclass(slots=True)
class ClickTask:
    x: int
    y: int
    delay: float

class ClickProcessor:
    """Optimized click execution using slot-based data structures."""
    def __init__(self):
        self._running = False
        self._lock = threading.Lock()

    def execute_sequence(self, tasks: list[ClickTask]):
        """Executes click sequence with minimal object overhead."""
        self._running = True
        try:
            for task in tasks:
                if not self._running:
                    break
                self._perform_click(task.x, task.y)
                time.sleep(task.delay)
        finally:
            self._running = False

    def _perform_click(self, x: int, y: int):
        """Mock low-level click event."""
        # Direct system call interface would go here
        pass

    def stop(self):
        with self._lock:
            self._running = False

def get_optimized_processor() -> ClickProcessor:
    """Factory for pre-configured click processor."""
    return ClickProcessor()