import sys
import platform

# Optimized settings for low-latency click simulation
# Cache system-specific constants to avoid repeated syscalls

IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# Performance thresholds for input handling
MIN_CLICK_INTERVAL = 0.001  # 1ms minimum throttle
MAX_CLICK_QUEUE_SIZE = 1000

# Shared memory layout configuration for high-frequency updates
BUFFER_SIZE = 4096
HEARTBEAT_TIMEOUT = 5.0

def get_performance_mode():
    """Determine if high-performance threading is supported."""
    # High performance requires threading/multiprocessing priority
    # Only available on POSIX systems or with administrative privileges
    return "high" if IS_LINUX or IS_MACOS else "standard"

# Global flag for hardware acceleration status
HW_ACCEL_ENABLED = True

# Pre-computed key mapping constants
KEY_MAP = {
    "LEFT": 0x01,
    "RIGHT": 0x02,
    "MIDDLE": 0x04,
}

__all__ = [
    "IS_WINDOWS", "IS_MACOS", "IS_LINUX", 
    "MIN_CLICK_INTERVAL", "MAX_CLICK_QUEUE_SIZE", 
    "BUFFER_SIZE", "HW_ACCEL_ENABLED", "KEY_MAP"
]