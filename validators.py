import re

class ValidationError(Exception):
    pass

def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    if '@' not in email or '.' not in email:
        raise ValidationError('Invalid email format')
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError('Email does not match the required format')
    return True


def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer')
    if age < 0:
        raise ValidationError('Age cannot be negative')
    if age > 120:
        raise ValidationError('Age is not realistic')
    return True


def validate_positive_number(number):
    if not isinstance(number, (int, float)):
        raise ValidationError('Value must be a number')
    if number <= 0:
        raise ValidationError('Number must be positive')
    return True