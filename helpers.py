def validate_click_settings(interval, duration):
    """
    Validates user input parameters for the autoclicker loop.
    """
    if not isinstance(interval, (int, float)) or not isinstance(duration, (int, float)):
        return False, "Input parameters must be numeric"
    
    if interval < 0.01:
        return False, "Interval too low, must be at least 0.01 seconds"
        
    if duration < 0:
        return False, "Duration cannot be negative"
        
    return True, "Success"

def process_input_validation(raw_interval, raw_duration):
    """
    Interface to parse and validate autoclicker parameters.
    """
    try:
        interval = float(raw_interval)
        duration = float(raw_duration)
    except (ValueError, TypeError):
        return None, "Invalid numeric input format"
        
    is_valid, message = validate_click_settings(interval, duration)
    if not is_valid:
        return None, message
        
    return (interval, duration), "Valid settings initialized"