import time
import pyautogui

def validate_inputs(clicks, interval):
    """Ensures inputs are within safe operating bounds."""
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError("Click count must be a positive integer.")
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be at least 0.01 seconds.")
    return True

def process_autoclick(clicks, interval):
    """Executes the main click loop with validation."""
    try:
        validate_inputs(clicks, interval)
        print(f"Starting autoclick: {clicks} clicks at {interval}s interval")
        
        for i in range(clicks):
            pyautogui.click()
            time.sleep(interval)
            
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected processing error: {e}")

if __name__ == "__main__":
    # Example usage for demonstration
    process_autoclick(5, 0.5)