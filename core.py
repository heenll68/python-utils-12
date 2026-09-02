import time
import sys

def run_autoclicker(clicks: int = 100, interval: float = 0.1, pos_x: int = None, pos_y: int = None):
    """Core autoclicker function with comprehensive error handling."""

    # Validate inputs for edge cases
    if not isinstance(clicks, int) or clicks < 1:
        raise ValueError("Number of clicks must be a positive integer")
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError("Interval must be a positive number")
    if pos_x is not None:
        if not isinstance(pos_x, int) or pos_x < 0:
            raise ValueError("X position must be a non-negative integer")
    if pos_y is not None:
        if not isinstance(pos_y, int) or pos_y < 0:
            raise ValueError("Y position must be a non-negative integer")

    click_counter = 0

    try:
        print(f"Autoclicker started: {clicks} clicks at {interval}s intervals")
        for i in range(clicks):
            try:
                # Simulate performing the click
                if pos_x is not None and pos_y is not None:
                    print(f"Performing click {i + 1} at position ({pos_x}, {pos_y})")
                else:
                    print(f"Performing click {i + 1} at current cursor position")
                # In a real implementation: pyautogui.click(x=pos_x, y=pos_y)
                time.sleep(interval)
                click_counter += 1
            except Exception as click_error:
                # Handle errors during individual clicks, e.g. permission or hardware issues
                print(f"Error on click {i + 1}: {click_error}. Continuing...")
                continue
    except KeyboardInterrupt:
        print("\nAutoclicker interrupted by user. Stopping gracefully.")
    except Exception as e:
        print(f"Unexpected error in autoclicker: {e}")
    finally:
        print(f"Autoclicker completed. Total successful clicks: {click_counter}")

if __name__ == "__main__":
    try:
        # Example usage with valid params
        run_autoclicker(clicks=10, interval=0.05, pos_x=500, pos_y=300)
    except ValueError as val_err:
        print(f"Invalid configuration: {val_err}")
        sys.exit(1)