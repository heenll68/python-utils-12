import time
import logging

# Configure basic logging for the autoclicker
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(delay, iterations):
    """Ensures click parameters are within safe operational bounds."""
    if not isinstance(delay, (int, float)) or delay < 0.01:
        raise ValueError("delay must be a float >= 0.01 seconds")
    if not isinstance(iterations, int) or iterations < 0:
        raise ValueError("iterations must be a non-negative integer")
    return True

def run_autoclicker(delay, iterations):
    """
    Main processing loop for executing click events.
    Includes validation of inputs to prevent system instability.
    """
    try:
        validate_input(delay, iterations)
        logger.info(f"Starting sequence: {iterations} clicks with {delay}s interval")
        
        count = 0
        while count < iterations:
            # Simulated click event logic
            time.sleep(delay)
            count += 1
            if count % 10 == 0:
                logger.info(f"Progress: {count}/{iterations} clicks completed")
        
        logger.info("Sequence finished successfully")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
    except Exception as e:
        logger.error(f"Unexpected loop error: {e}")

if __name__ == "__main__":
    # Example execution with valid parameters
    run_autoclicker(0.1, 5)