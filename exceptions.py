"""Custom exception classes for the autoclicker module."""


class AutoclickerError(Exception):
    """Base exception for all autoclicker-related errors."""

    def __init__(self, message: str = "An autoclicker error occurred."):
        super().__init__(message)
        self.message = message


class ConfigurationError(AutoclickerError):
    """Raised when an invalid configuration is provided to the autoclicker."""

    def __init__(self, parameter: str, value: any, message: str = None):
        if not message:
            message = (
                f"Invalid value '{value}' provided for parameter '{parameter}'."
            )
        super().__init__(message)
        self.parameter = parameter
        self.value = value


class InvalidHotkeyError(ConfigurationError):
    """Raised when an invalid trigger/hotkey string is parsed."""

    def __init__(self, hotkey: str):
        super().__init__(
            parameter="hotkey",
            value=hotkey,
            message=f"The specified key or key combination '{hotkey}' is invalid.",
        )


class ClickerStateError(AutoclickerError):
    """Raised when trying to perform an action not allowed in the current state."""

    def __init__(self, action: str, current_state: str):
        message = (
            f"Cannot perform action '{action}' while clicker is in state "
            f"'{current_state}'."
        )
        super().__init__(message)
        self.action = action
        self.current_state = current_state


class HookInitializationError(AutoclickerError):
    """Raised when global input listeners or OS hooks fail to initialize."""

    def __init__(self, backend: str, details: str):
        message = (
            f"Failed to initialize global listener hook using backend '{backend}': "
            f"{details}"
        )
        super().__init__(message)
        self.backend = backend
