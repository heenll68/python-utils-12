class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small."""
    def __init__(self, message="Value is too small"):  
        self.message = message
        super().__init__(self.message)

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large."""
    def __init__(self, message="Value is too large"):  
        self.message = message
        super().__init__(self.message)

# Function to check the input value

def check_value(value):
    try:
        if value < 10:
            raise ValueTooSmallError()
        elif value > 100:
            raise ValueTooLargeError()
        else:
            return "Value is within the acceptable range!"
    except CustomError as e:
        return str(e)

# Example usage
if __name__ == '__main__':
    print(check_value(5))   # Value is too small
    print(check_value(150)) # Value is too large
    print(check_value(50))  # Value is within the acceptable range!