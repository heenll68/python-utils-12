# python-utils-12: Advanced Python Autoclicker

`python-utils-12` is a high-performance, cross-platform autoclicker designed to streamline repetitive desktop tasks with minimal CPU overhead. It utilizes low-level system hooks to provide reliable input automation for Windows, macOS, and Linux environments.

### Features
*   **Dynamic CPS Control:** Precision-adjust your clicks per second (CPS) via an intuitive CLI interface.
*   **Smart Hotkeys:** Global toggle functionality allows you to start or stop automation instantly, even when the terminal is unfocused.
*   **Variable Click Modes:** Supports left, right, and middle mouse button emulation with adjustable randomized delays to mimic human interaction.
*   **Minimalist Architecture:** Built on lightweight dependencies (`pynput`) to ensure high stability and negligible system impact.

### Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-12.git
cd python-utils-12
pip install -r requirements.txt
```

### Usage

Run the utility directly from your terminal. You can define the click interval (in seconds) via the `--interval` flag:

```bash
# Example: Click once every 0.5 seconds
python main.py --interval 0.5
```

**Hotkeys:**
*   **F6:** Start/Resume automation.
*   **F7:** Stop automation.
*   **Ctrl+C:** Exit the application.

### License

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.