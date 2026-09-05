import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class AutoClickerConfig:
    """Configuration settings for the autoclicker application."""

    interval: float = 0.1
    button: str = "left"
    clicks: int = 0
    hotkey: str = "f8"
    random_delay_range: float = 0.02

    def validate(self) -> bool:
        """Validate configuration values for safe execution."""
        if self.interval <= 0:
            raise ValueError("Interval must be a positive number.")
        if self.button not in ("left", "right", "middle"):
            raise ValueError(
                f"Invalid mouse button: {self.button}. Must be 'left', 'right', or 'middle'."
            )
        if self.clicks < 0:
            raise ValueError("Clicks count cannot be negative.")
        if self.random_delay_range < 0:
            raise ValueError("Random delay range cannot be negative.")
        return True

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration options to a dictionary."""
        return asdict(self)

    def save_to_file(self, file_path: Path) -> None:
        """Save configuration parameters to a JSON file."""
        self.validate()
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load_from_file(cls, file_path: Path) -> "AutoClickerConfig":
        """Load configuration parameters from a JSON file."""
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        config = cls(**data)
        config.validate()
        return config
