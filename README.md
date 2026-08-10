# python-utils-12

A collection of handy utility functions designed to streamline common programming tasks in Python. Whether you are an experienced developer or a beginner, these tools will help improve your code efficiency and reduce redundancy.

## Features
- **Data Validation**: Easily validate user input with predefined checks for various data types, including strings, integers, and dates.
- **File Management**: Simplify operations like reading, writing, and deleting files with a set of straightforward functions that handle exceptions gracefully.
- **String Manipulation**: Access a suite of string functions for formatting, searching, and transforming text to enhance your data processing capabilities.
- **Logging Utilities**: Implement consistent logging practices across your projects with built-in customizable logging functions.

## Installation

To install the package, use pip:

```bash
pip install python-utils-12
```

Alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install .
```

## Basic Usage Example

Here's a quick example demonstrating the usage of the utilities provided:

```python
from utils import validate_email, read_file, write_file, log_info

# Validate an email address
email = "example@mail.com"
if validate_email(email):
    log_info(f"{email} is valid!")
else:
    log_info(f"{email} is not valid.")

# Read from a file
content = read_file("example.txt")
print(content)

# Write to a file
write_file("output.txt", "This is an example output.")
```

## License

![License](https://img.shields.io/badge/license-MIT-green)  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.