class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'{resource} not found'
        super().__init__(self.message)

class PermissionError(CustomError):
    """Raised when permission is denied."""
    def __init__(self, action):
        self.action = action
        self.message = f'Permission denied for action: {action}'
        super().__init__(self.message)

# Example usage
if __name__ == '__main__':
    try:
        raise ValidationError('Input data is invalid')
    except ValidationError as e:
        print(e)  # Output: Input data is invalid
    try:
        raise NotFoundError('User')
    except NotFoundError as e:
        print(e)  # Output: User not found
