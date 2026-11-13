[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# python-utils-12

`python-utils-12` is a high-performance, lightweight mouse automation utility engineered for high-frequency clicking and macro execution. Built in Python, it delivers precise click-timing controls alongside global hotkey listeners for seamless background operation.

## Features

* **Sub-Millisecond Precision:** Dynamic click-rate configuration supporting 1 to 1,000+ clicks per second (CPS) with optional micro-jitter to mimic human input patterns.
* **Global Hotkey Binds:** Instant start, pause, and emergency kill-switch controls active across all system windows.
* **Coordinate Targeting:** Support for locked-position clicking, relative offset sequences, and active cursor tracking modes.
* **Low System Overhead:** Native C-type event dispatching via `pynput` ensuring near-zero CPU and RAM impact during continuous loops.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install -r requirements.txt
```

## Quick Start

Run the autoclicker via CLI with standard parameters:

```bash
python main.py --cps 50 --button left --hotkey f6
```

Or import the module directly into your Python scripts:

```python
from python_utils_12 import ClickerEngine

# Initialize engine: 100 CPS on left mouse button
engine = ClickerEngine(cps=100, button="left", randomized=True)

# Register F6 as the toggle key and start background listener
engine.set_hotkey("f6")
engine.start_listener()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.