import os
import platform
import socket


def get_system_info() -> dict[str, str]:
    return {
        "hostname": socket.gethostname(),
        "user": os.getenv("USER", "unknown"),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
    }
