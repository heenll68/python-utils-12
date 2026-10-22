# python-utils-12: Advanced Python Autoclicker

`python-utils-12` is a high-performance, cross-platform automation tool built to simulate mouse input with millisecond precision. It provides a lightweight, scriptable interface for repetitive GUI tasks, desktop gaming, and automated testing workflows.

## Features

*   **Configurable Interval Control:** Set precise delay thresholds between clicks to bypass basic rate-limiting while maintaining high efficiency.
*   **Dynamic Mouse Mapping:** Support for both coordinate-based clicking and "current cursor position" modes.
*   **Kill-Switch Integration:** Built-in safety mechanisms that immediately terminate automation upon pressing a designated panic key.
*   **Low-Overhead Execution:** Minimal CPU footprint optimized for background operation during long-running sessions.

## Installation

Ensure you have Python 3.8+ installed. You can set up the utility via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12

# Install required dependencies
pip install -r requirements.txt
```

## Basic Usage

To initiate a standard autoclicker session at 50ms intervals, use the following command:

```python
from utils import AutoClicker

# Initialize with 50ms delay
bot = AutoClicker(interval=0.05)

# Start clicking at current mouse location
bot.start()

# Stop clicking by pressing 'q'
```

For advanced users, you can pass custom coordinate tuples:

```python
# Click specifically at (500, 500)
bot.click_at(x=500, y=500, duration=10)
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.