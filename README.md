# python-utils-12: Advanced Python Autoclicker

`python-utils-12` is a high-performance, cross-platform automation utility designed to simulate mouse input with precision. It provides a clean, scriptable interface for automating repetitive clicking tasks in desktop environments.

## Features

*   **Configurable Intervals:** Set precise delays between clicks (in milliseconds) to mimic human-like behavior or maximize speed.
*   **Dynamic Targeting:** Easily define coordinates or track the current cursor position for relative clicking.
*   **Safe-Stop Mechanism:** Built-in emergency stop via keyboard hotkey to instantly terminate execution during automated cycles.
*   **Low Latency:** Optimized for minimal resource consumption, ensuring stability during long-running background tasks.

## Installation

Ensure you have Python 3.8+ installed. You can install the required dependencies via pip:

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install -r requirements.txt
```

## Usage

You can launch the autoclicker directly from the CLI. Below is an example of how to configure an automated clicking session:

```python
from utils import AutoClicker

# Initialize with 100ms interval
bot = AutoClicker(interval=0.1)

# Start clicking at the current cursor position
bot.start(button='left', count=500)
```

To run a pre-defined configuration script:

```bash
python main.py --config settings.json
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.