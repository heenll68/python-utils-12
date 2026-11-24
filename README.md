# python-utils-12: Advanced Python Autoclicker

`python-utils-12` is a lightweight, high-performance automation utility designed to execute repetitive mouse clicks with precision. It provides a clean command-line interface for automating tasks ranging from gaming inputs to workflow optimization.

### Key Features

*   **Configurable Intervals:** Set precise click delays in milliseconds to mimic human behavior or maximize speed.
*   **Dynamic Mouse Control:** Supports both single-click and toggle-mode clicking with custom trigger hotkeys.
*   **Coordinate Locking:** Lock the cursor to specific X/Y screen coordinates for repetitive UI interactions.
*   **Cross-Platform Support:** Built with `pynput` to ensure seamless functionality across Windows, macOS, and Linux.

### Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install -r requirements.txt
```

### Basic Usage

To start the autoclicker with a default delay of 100ms, run the following command:

```bash
python main.py --interval 0.1 --button left
```

For advanced usage, you can define specific screen coordinates:

```bash
# Clicks at X=500, Y=500 with a 50ms delay
python main.py --x 500 --y 500 --interval 0.05
```

Press `Ctrl+C` in your terminal to safely terminate the automation script at any time.

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.