import logging

def validate_click_params(interval, count):
    """Ensures input parameters are within operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logging.error(f"Invalid interval: {interval}. Must be >= 0.01.")
        return False
    if not isinstance(count, int) or count < -1:
        logging.error(f"Invalid count: {count}. Must be -1 or positive.")
        return False
    return True

def process_input_loop(params):
    """Main loop interface with safety checks."""
    interval = params.get("interval", 0.1)
    count = params.get("count", 1)

    if not validate_click_params(interval, count):
        raise ValueError("Parameter validation failure in autoclicker loop")

    print(f"Processing clicks: interval={interval}, count={count}")
    return True

if __name__ == "__main__":
    # Example usage for validation testing
    test_params = {"interval": 0.5, "count": 10}
    try:
        process_input_loop(test_params)
    except ValueError as e:
        print(f"Caught expected error: {e}")