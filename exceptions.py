import time
import requests

class NetworkError(Exception):
    pass


def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1}/{retries} failed: {e}')
            time.sleep(delay)  # Wait before the next attempt
    raise NetworkError(f'Failed to fetch data from {url} after {retries} attempts')
