import time
import requests

class NetworkOperationError(Exception):
    pass

def retry_on_failure(max_retries=3, backoff_factor=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except NetworkOperationError:
                    attempts += 1
                    wait_time = backoff_factor ** attempts
                    print(f'Retrying {func.__name__}: attempt {attempts} in {wait_time}s')
                    time.sleep(wait_time)
            raise NetworkOperationError(f'Max retries exceeded for {func.__name__}')
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, backoff_factor=2)
def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise NetworkOperationError(f'Error fetching data: {response.status_code}')
    return response.json()  

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except NetworkOperationError as e:
        print(e)