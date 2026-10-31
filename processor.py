import json
import time
from typing import List, Dict, Any

class ClickDataProcessor:
    """Processes and normalizes click sequences for autoclicker playback."""

    def __init__(self, min_interval_ms: float = 10.0, default_button: str = "left"):
        self.min_interval_ms = min_interval_ms
        self.default_button = default_button

    def sanitize_sequence(self, raw_clicks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validates and cleans raw click sequence data."""
        processed = []
        for item in raw_clicks:
            x = max(0, int(item.get("x", 0)))
            y = max(0, int(item.get("y", 0)))
            delay = float(item.get("delay_ms", self.min_interval_ms))
            if delay < self.min_interval_ms:
                delay = self.min_interval_ms

            button = str(item.get("button", self.default_button)).lower()
            if button not in ("left", "right", "middle"):
                button = self.default_button

            processed.append({
                "x": x,
                "y": y,
                "delay_ms": delay,
                "button": button,
                "double": bool(item.get("double", False))
            })
        return processed

    def export_profile(self, profile_name: str, click_data: List[Dict[str, Any]]) -> str:
        """Formats processed click sequence into a serialized profile string."""
        sanitized = self.sanitize_sequence(click_data)
        payload = {
            "profile_name": profile_name,
            "version": "1.2",
            "created_at": time.time(),
            "clicks": sanitized,
            "total_clicks": len(sanitized)
        }
        return json.dumps(payload, indent=2)
