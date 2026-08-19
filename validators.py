import re

class InputValidator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_url(url: str) -> bool:
        url_regex = r'^(https?|ftp)://[^
/$.?#].[^
]*$'
        return re.match(url_regex, url) is not None

    @staticmethod
    def is_positive_integer(value: str) -> bool:
        return value.isdigit() and int(value) > 0

    @staticmethod
    def are_valid_inputs(inputs: dict) -> bool:
        return (InputValidator.is_valid_email(inputs.get('email', '')) and
                InputValidator.is_valid_url(inputs.get('url', '')) and
                InputValidator.is_positive_integer(inputs.get('count', '')))  

# Example usage:
if __name__ == '__main__':
    inputs = {'email': 'example@test.com', 'url': 'https://www.example.com', 'count': '5'}
    print(InputValidator.are_valid_inputs(inputs))  # Should return True