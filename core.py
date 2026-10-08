import time
import threading
from typing import Callable, Optional

class FastAutoclicker:
    '''High-performance click loop with high-resolution timing calibration.'''
    def __init__(self, click_action: Callable[[], None], interval: float = 0.001):
        self.click_action = click_action
        self.interval = interval
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def start(self) -> None:
        '''Starts the autoclicking loop in a background thread.'''
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        '''Stops the autoclicking loop.'''
        self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)

    def _loop(self) -> None:
        '''Optimized timing loop using hybrid sleeping/spinning for precision.'''
        target_interval = self.interval
        click = self.click_action
        
        # Local variable cache for maximizing loop performance
        perf_counter = time.perf_counter
        sleep = time.sleep

        last_time = perf_counter()
        while self._running:
            now = perf_counter()
            elapsed = now - last_time
            
            if elapsed >= target_interval:
                click()
                # Prevent cumulative delay drift
                last_time = now - min(elapsed - target_interval, target_interval)
                
                # Sleep short of target time to accommodate OS scheduler overhead
                if target_interval > 0.002:
                    sleep(target_interval - 0.001)
            else:
                # Avoid CPU choking while keeping precision intact
                remaining = target_interval - elapsed
                if remaining > 0.0015:
                    sleep(0.001)
