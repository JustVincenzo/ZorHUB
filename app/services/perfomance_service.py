import psutil


def get_performance_metrics() -> dict[str, float | int]:
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "ram_percent": memory.percent,
        "ram_used_gb": round(memory.used / (1024 ** 3), 2),
        "ram_total_gb": round(memory.total / (1024 ** 3), 2),
        "swap_percent": swap.percent,
        "process_count": len(psutil.pids()),
    }


def describe_performance(metrics: dict[str, float | int]) -> tuple[str, str]:
    cpu = float(metrics.get("cpu_percent", 0))
    ram = float(metrics.get("ram_percent", 0))

    if cpu >= 90 or ram >= 90:
        return "High load", "Your system is using a very high amount of resources."
    if cpu >= 70 or ram >= 80:
        return "Moderate load", "Your system is working harder than usual."
    return "Normal", "Your computer is responding within expected resource usage."
