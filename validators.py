import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, backoff_factor=0.3):
    """
    Make a GET request to the specified URL, with retry logic.
    Args:
        url (str): The URL to request.
        max_retries (int): Maximum number of retries.
        backoff_factor (float): Factor to increase wait time between retries.
    Returns:
        responses (Response): The response from the GET request.
    Raises:
        Exception: If all retries fail.
    """
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response
        except RequestException as e:
            retries += 1
            wait = backoff_factor * (2 ** (retries - 1))
            time.sleep(wait)  # Exponential backoff
            if retries == max_retries:
                raise Exception(f'Request failed after {max_retries} retries: {e}')  
    return None

# Example usage:
#if __name__ == '__main__':
#    try:
#        response = retry_request('http://example.com')
#        print(response.text)
#    except Exception as error:
#        print(error)