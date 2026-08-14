import logging
import os

class Logger:
    def __init__(self, log_file='app.log'):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(log_file)
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            print(f'Error logging info: {e}')  # prints to stdout

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            print(f'Error logging warning: {e}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            print(f'Error logging error: {e}')

    def log_debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            print(f'Error logging debug: {e}')

    def close(self):
        try:
            self.handler.close()
            self.logger.removeHandler(self.handler)
        except Exception as e:
            print(f'Error closing logger: {e}')