# python-utils-12

An efficient, cross-platform autoclicker built in Python designed for task automation and repetitive interface testing. This utility provides a lightweight interface to simulate precise mouse events with customizable intervals and trigger conditions.

## Features

*   **Configurable Interval Control:** Set precise delay timings between clicks in milliseconds to match any application requirement.
*   **Dynamic Trigger System:** Use customizable hotkeys to toggle the autoclicker state instantly without interrupting your workflow.
*   **Target Mode:** Capture and lock onto specific screen coordinates or follow the current mouse position.
*   **Resource Optimized:** Built with minimal dependencies to ensure low CPU and memory overhead during long-running background tasks.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone the repository and install the required dependencies via pip:

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install -r requirements.txt
```

## Usage

To start the autoclicker with default settings, run the following command from your terminal:

```bash
python main.py --interval 0.5 --button left
```

### Example
To set a custom click interval of 100ms and bind the start/stop function to the 'F8' key, use the following configuration:

```python
from utils import AutoClicker

bot = AutoClicker(interval=0.1, key='f8')
bot.run()
```

*Note: You may need to run your terminal or IDE with administrative privileges on Windows/macOS to allow the script to interact with global system input events.*

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.