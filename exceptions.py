"""Custom exceptions for the autoclicker utility."""


class AutoclickerError(Exception):
    """Base exception class for all autoclicker errors."""

    def __init__(self, message="An autoclicker error occurred"):
        self.message = message
        super().__init__(self.message)


class ConfigurationError(AutoclickerError):
    """Raised when there is an invalid parameter configuration."""

    def __init__(self, parameter, value, message=None):
        self.parameter = parameter
        self.value = value
        error_msg = (
            message
            or f"Invalid value '{value}' for configuration parameter '{parameter}'"
        )
        super().__init__(error_msg)


class PermissionError(AutoclickerError):
    """Raised when OS-level permissions are missing."""

    def __init__(self, target_os, message=None):
        self.target_os = target_os
        error_msg = (
            message or f"Insufficient permissions to control input on {target_os}"
        )
        super().__init__(error_msg)


class ControllerStateError(AutoclickerError):
    """Raised when a state transition is invalid."""

    def __init__(self, current_state, action):
        self.current_state = current_state
        self.action = action
        error_msg = (
            f"Cannot perform action '{action}' while in state '{current_state}'"
        )
        super().__init__(error_msg)


class DeviceHookError(AutoclickerError):
    """Raised when listener or clicker hooks fail to register."""

    def __init__(self, device_type="mouse or keyboard"):
        error_msg = f"Failed to bind hook to system {device_type}"
        super().__init__(error_msg)
