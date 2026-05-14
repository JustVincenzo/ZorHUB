import psutil


def get_storage_metrics(path: str = "/") -> dict[str, float | str]:
    usage = psutil.disk_usage(path)
    return {
        "path": path,
        "disk_percent": usage.percent,
        "disk_used_gb": round(usage.used / (1024 ** 3), 2),
        "disk_total_gb": round(usage.total / (1024 ** 3), 2),
        "disk_free_gb": round(usage.free / (1024 ** 3), 2),
    }


def describe_storage(metrics: dict[str, float | str]) -> tuple[str, str]:
    percent = float(metrics.get("disk_percent", 0))
    if percent >= 90:
        return "Storage critical", "Your disk is almost full. Updates and installations may fail."
    if percent >= 80:
        return "Storage high", "Your disk is close to the recommended limit."
    return "Storage normal", "Your disk has enough free space for normal use."
