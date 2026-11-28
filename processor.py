import time
import logging

def validate_inputs(clicks, interval):
    """Ensures click count and interval are positive numbers."""
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError("Click count must be a positive integer")
    if not isinstance(interval, (int, float)) or interval < 0:
        raise ValueError("Interval must be a non-negative number")

def run_autoclicker(clicks: int, interval: float):
    """Main processing loop for executing clicks."""
    try:
        validate_inputs(clicks, interval)
        
        logging.info(f"Starting autoclicker: {clicks} clicks at {interval}s interval")
        
        for i in range(clicks):
            # Simulating click action
            print(f"Click action triggered: {i + 1}/{clicks}")
            
            if interval > 0:
                time.sleep(interval)
                
    except ValueError as e:
        logging.error(f"Validation failure: {e}")
    except KeyboardInterrupt:
        logging.info("Process interrupted by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_autoclicker(5, 0.5)