import pyautogui
from typing import Tuple, Union


def get_screen_bounds() -> Tuple[int, int]:
    """Retrieve the current primary screen resolution safely."""
    try:
        width, height = pyautogui.size()
        return width, height
    except Exception:
        # Fallback to standard 1080p if screen resolution detection fails
        return 1920, 1080


def validate_coordinates(x: Union[int, float], y: Union[int, float]) -> Tuple[int, int]:
    """
    Validate and clamp screen coordinates within display bounds.
    Handles non-numeric, negative, or out-of-bounds inputs.
    """
    max_w, max_h = get_screen_bounds()

    try:
        clean_x = int(round(float(x)))
        clean_y = int(round(float(y)))
    except (ValueError, TypeError):
        # Default to screen center if coordinate parsing fails
        return max_w // 2, max_h // 2

    # Clamp coordinates strictly inside display boundary
    clamped_x = max(0, min(clean_x, max_w - 1))
    clamped_y = max(0, min(clean_y, max_h - 1))

    return clamped_x, clamped_y


def safe_interval(interval: Union[int, float], min_limit: float = 0.001) -> float:
    """Ensure click interval is a non-negative float above safety threshold."""
    try:
        val = float(interval)
        return max(val, min_limit)
    except (ValueError, TypeError):
        return 0.1  # Safe default fallback interval (100ms)


def sanitize_button_name(button: str) -> str:
    """Normalize and validate mouse button choices."""
    valid_buttons = {"left", "right", "middle"}
    if not isinstance(button, str):
        return "left"

    clean_btn = button.strip().lower()
    return clean_btn if clean_btn in valid_buttons else "left"
