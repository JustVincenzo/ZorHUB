import shutil
import subprocess
import psutil


def get_battery_status() -> dict[str, str | float | bool]:
    battery = psutil.sensors_battery()
    if battery is None:
        return {"available": False, "status": "Not available"}
    return {
        "available": True,
        "percent": round(battery.percent, 1),
        "charging": bool(battery.power_plugged),
        "status": "Charging" if battery.power_plugged else "Discharging",
    }


def get_power_profile() -> dict[str, str | bool]:
    if shutil.which("powerprofilesctl") is None:
        return {"available": False, "profile": "Not available"}
    try:
        result = subprocess.run(
            ["powerprofilesctl", "get"],
            text=True,
            capture_output=True,
            timeout=2,
            check=False,
        )
        profile = result.stdout.strip() or "unknown"
        return {"available": True, "profile": profile}
    except Exception:
        return {"available": False, "profile": "Unknown"}
