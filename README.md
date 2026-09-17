# python-utils-12: Advanced Python Autoclicker

`python-utils-12` is a lightweight, high-performance automation utility designed for rapid-fire mouse event simulation in Python. It provides a robust framework for repetitive task automation without the overhead of heavy GUI-based software.

### Features

*   **Configurable CPS:** Dynamically adjust clicks per second to meet specific application requirements.
*   **Hotkey Support:** Integrated key listener to toggle automation states instantly during runtime.
*   **Precision Targeting:** Coordinates-based clicking with optional randomization to mimic human-like behavior.
*   **Cross-Platform Compatibility:** Built on `pynput` to ensure seamless performance across Windows, macOS, and Linux.

### Installation

Ensure you have Python 3.8+ installed. You can install the required dependencies using `pip`:

```bash
# Clone the repository
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12

# Install dependencies
pip install -r requirements.txt
```

### Usage

To start the autoclicker with a default configuration of 10 clicks per second, run the following command from the terminal:

```python
from utils import AutoClicker

# Initialize with 10 clicks per second
clicker = AutoClicker(cps=10)

# Start clicking at current mouse position until toggled off
clicker.start()
```

You can also bind the automation to a specific trigger key:

```python
# Start on 'f6' key press
clicker.set_hotkey('f6')
clicker.listen()
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Disclaimer: Use this tool responsibly. The author is not responsible for any violation of terms of service in third-party applications resulting from the use of this utility.*