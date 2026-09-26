import time
from typing import Dict, Any, List, Optional


class ClickTaskProcessor:
    """Processes and validates autoclicker task parameters in the execution loop."""

    ALLOWED_BUTTONS = {"left", "right", "middle"}

    def __init__(self, min_interval: float = 0.01, max_clicks: int = 10000):
        self.min_interval = min_interval
        self.max_clicks = max_clicks

    def validate_task_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validates raw task parameters and returns normalized config."""
        interval = float(config.get("interval", 0.1))
        if interval < self.min_interval:
            raise ValueError(f"Interval {interval}s below minimum safe limit of {self.min_interval}s")

        clicks = int(config.get("clicks", 10))
        if clicks <= 0 or clicks > self.max_clicks:
            raise ValueError(f"Clicks count {clicks} must be between 1 and {self.max_clicks}")

        button = str(config.get("button", "left")).lower()
        if button not in self.ALLOWED_BUTTONS:
            raise ValueError(f"Invalid button '{button}'. Allowed: {self.ALLOWED_BUTTONS}")

        coords = config.get("coordinates")
        if coords is not None:
            if not (isinstance(coords, (tuple, list)) and len(coords) == 2):
                raise ValueError("Coordinates must be a tuple/list of two integers (x, y)")
            x, y = coords
            if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
                raise ValueError(f"Invalid screen coordinates: ({x}, {y})")

        return {
            "interval": interval,
            "clicks": clicks,
            "button": button,
            "coordinates": tuple(coords) if coords else None,
        }

    def process_queue(self, task_queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop with input validation for queued click tasks."""
        processed_results = []

        for index, raw_task in enumerate(task_queue):
            try:
                valid_config = self.validate_task_config(raw_task)
                processed_results.append({
                    "task_id": index,
                    "status": "validated",
                    "config": valid_config
                })
            except (ValueError, TypeError) as err:
                processed_results.append({
                    "task_id": index,
                    "status": "failed",
                    "error": str(err)
                })

        return processed_results
