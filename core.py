import time
import pyautogui

def validate_params(clicks, interval):
    """Ensures input values are within operational bounds."""
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError("Click count must be a positive integer")
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be at least 0.01 seconds")

def run_autoclicker(clicks, interval):
    """
    Main processing loop with input validation.
    Executes specified number of clicks at set interval.
    """
    try:
        validate_params(clicks, interval)
        print(f"Starting autoclicker: {clicks} clicks at {interval}s interval")
        
        for _ in range(clicks):
            pyautogui.click()
            time.sleep(interval)
            
        print("Processing complete.")
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Example usage with validated parameters
    run_autoclicker(clicks=5, interval=0.5)