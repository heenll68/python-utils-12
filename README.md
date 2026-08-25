[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-12

python-utils-12 is a Python-based autoclicker designed to automate repetitive mouse clicking tasks with high precision. It features customizable intervals, hotkey controls, and session tracking for efficient automation in various scenarios.

## Features

- Millisecond-accurate click timing with optional randomization to simulate natural input
- Flexible button selection for left-click, right-click, and double-click actions
- Global hotkeys to toggle the autoclicker without switching windows
- Detailed logging that saves click counts, intervals used, and total runtime to a file

## Installation

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install -r requirements.txt
```

## Usage

Run the autoclicker from the command line:

```bash
python main.py --interval 0.1 --clicks 1000 --button left
```

For programmatic use:

```python
from python_utils_12 import AutoClicker

clicker = AutoClicker(interval=0.5, button="right", max_clicks=100)
clicker.start()
```