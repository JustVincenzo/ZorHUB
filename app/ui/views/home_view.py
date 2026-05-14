import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.services.performance_service import get_performance_metrics, describe_performance
from app.services.storage_service import get_storage_metrics, describe_storage
from app.services.power_service import get_battery_status, get_power_profile
from app.ui.widgets.status_card import StatusCard
from app.ui.widgets.metric_card import MetricCard


class HomeView(Gtk.ScrolledWindow):
    def __init__(self) -> None:
        super().__init__()
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)

        title = Gtk.Label(label="Home")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        content.append(title)

        perf = get_performance_metrics()
        storage = get_storage_metrics()
        battery = get_battery_status()
        power = get_power_profile()
        _perf_status, perf_msg = describe_performance(perf)
        _storage_status, storage_msg = describe_storage(storage)

        score = self._calculate_score(float(perf["cpu_percent"]), float(perf["ram_percent"]), float(storage["disk_percent"]))
        status_body = f"Good · {score}/100\n\n{perf_msg}\n{storage_msg}"
        content.append(StatusCard("System status", status_body))

        grid = Gtk.Grid(column_spacing=12, row_spacing=12)
        grid.attach(MetricCard("CPU", f"{perf['cpu_percent']}%"), 0, 0, 1, 1)
        grid.attach(MetricCard("RAM", f"{perf['ram_percent']}%", f"{perf['ram_used_gb']} GB / {perf['ram_total_gb']} GB"), 1, 0, 1, 1)
        grid.attach(MetricCard("Storage", f"{storage['disk_percent']}%", f"{storage['disk_free_gb']} GB free"), 0, 1, 1, 1)
        battery_text = "Not available" if not battery.get("available") else f"{battery['percent']}% · {battery['status']}"
        grid.attach(MetricCard("Battery", battery_text), 1, 1, 1, 1)
        content.append(grid)

        content.append(StatusCard("Energy mode", str(power.get("profile", "Not available"))))
        content.append(StatusCard("ZorHUB Agent", "Not installed. Advanced actions are disabled in this private pre-alpha."))

        self.set_child(content)

    def _calculate_score(self, cpu: float, ram: float, disk: float) -> int:
        score = 100
        if cpu > 70:
            score -= 10
        if cpu > 90:
            score -= 15
        if ram > 80:
            score -= 10
        if ram > 90:
            score -= 15
        if disk > 80:
            score -= 10
        if disk > 90:
            score -= 15
        return max(score, 0)
