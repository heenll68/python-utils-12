from pynput.mouse import Controller, Listener
import time

class AutoClicker:
    """Class to handle auto-clicking operations."""
    def __init__(self, interval: float):
        """Initialize the auto-clicker with a specified interval.
        
        Args:
            interval (float): Time in seconds between clicks.
        """
        self.interval = interval
        self.mouse = Controller()

    def click(self):
        """Perform a mouse click."""
        self.mouse.click(Button.left)

    def start(self):
        """Start the auto-clicking process."""
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x: int, y: int, button, pressed: bool):
        """Handle mouse click events.
        
        Args:
            x (int): The x-coordinate of the mouse click.
            y (int): The y-coordinate of the mouse click.
            button: The button that was pressed.
            pressed (bool): Whether the button was pressed or released.
        """
        if pressed:
            print(f'Clicking at ({x}, {y})')
            self.click()
            time.sleep(self.interval)

if __name__ == '__main__':
    autoclicker = AutoClicker(0.1)
    autoclicker.start()