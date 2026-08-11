import os
import json
import logging
from typing import Any, Dict

logging.basicConfig(level=logging.INFO)


def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load JSON file from a given filepath."""
    if not os.path.exists(filepath):
        logging.warning(f"File not found: {filepath}")
        return {}
    with open(filepath, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {filepath}: {e}")
            return {}


def save_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Save a dictionary as a JSON file to the given filepath."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
        logging.info(f"Data saved to {filepath}")


def clean_directory(directory: str) -> None:
    """Remove all files in the specified directory."""
    if not os.path.isdir(directory):
        logging.warning(f"Directory not found: {directory}")
        return
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                logging.info(f"Removed file: {file_path}")
        except Exception as e:
            logging.error(f"Error while removing {file_path}: {e}")
