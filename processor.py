import time
from typing import Dict, Any, Tuple, Optional


class ClickValidationError(Exception):
    """Raised when input parameters for click event fail validation."""
    pass


class ClickProcessor:
    """Processes autoclicker commands with strict input validation in the main loop."""

    ALLOWED_BUTTONS = {"left", "right", "middle"}
    MIN_INTERVAL = 0.001  # Minimum 1ms interval
    MAX_INTERVAL = 3600.0  # Maximum 1 hour

    def __init__(self):
        self.is_running = False

    def validate_click_config(self, config: Dict[str, Any]) -> Tuple[float, str, int, Optional[Tuple[int, int]]]:
        """Validates configuration parameters for click execution."""
        interval = config.get("interval", 0.1)
        if not isinstance(interval, (int, float)) or not (self.MIN_INTERVAL <= interval <= self.MAX_INTERVAL):
            raise ClickValidationError(f"Interval must be between {self.MIN_INTERVAL} and {self.MAX_INTERVAL} seconds.")

        button = config.get("button", "left")
        if not isinstance(button, str) or button.lower() not in self.ALLOWED_BUTTONS:
            raise ClickValidationError(f"Button must be one of: {', '.join(self.ALLOWED_BUTTONS)}.")

        clicks = config.get("clicks", 1)
        if not isinstance(clicks, int) or clicks < 0:
            raise ClickValidationError("Click count must be a non-negative integer.")

        position = config.get("position")
        if position is not None:
            if not (isinstance(position, (tuple, list)) and len(position) == 2):
                raise ClickValidationError("Position must be a tuple/list of two integers (x, y).")
            x, y = position
            if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
                raise ClickValidationError("Coordinates x and y must be non-negative integers.")
            position = (x, y)

        return float(interval), button.lower(), clicks, position

    def process_loop(self, raw_configs: list) -> int:
        """Main processing loop that validates each input configuration before execution."""
        self.is_running = True
        successful_clicks = 0

        for raw_cfg in raw_configs:
            if not self.is_running:
                break

            try:
                # Perform input validation step prior to task execution
                interval, button, clicks, pos = self.validate_click_config(raw_cfg)
                
                # Simulate executing validated click sequence
                print(f"Executing {clicks} '{button}' click(s) at {pos or 'current pos'} (interval: {interval}s)")
                successful_clicks += clicks
                time.sleep(min(interval, 0.05))
                
            except ClickValidationError as err:
                print(f"Skipping invalid click task: {err}")
                continue

        self.is_running = False
        return successful_clicks
