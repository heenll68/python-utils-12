import pyautogui
import time
import logging

class ClickProcessor:
    """Handles click operations and autoclicker execution loops."""
    
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.is_running = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ClickProcessor")

    def start(self, duration: int):
        """Executes mouse clicks for a specified duration."""
        self.is_running = True
        self.logger.info(f"Starting autoclicker for {duration} seconds")
        
        end_time = time.time() + duration
        try:
            while self.is_running and time.time() < end_time:
                pyautogui.click()
                time.sleep(self.interval)
        except Exception as e:
            self.logger.error(f"Click execution error: {e}")
        finally:
            self.stop()

    def stop(self):
        """Signals cessation of click operations."""
        self.is_running = False
        self.logger.info("Autoclicker stopped")

    def update_interval(self, new_interval: float):
        """Adjustment of delay between clicks."""
        if new_interval > 0:
            self.interval = new_interval
            self.logger.info(f"Interval updated to {new_interval}s")