import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.services.storage_service import get_storage_metrics, describe_storage
from app.ui.widgets.status_card import StatusCard
from app.ui.widgets.metric_card import MetricCard


class StorageView(Gtk.ScrolledWindow):
    def __init__(self) -> None:
        super().__init__()
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)

        title = Gtk.Label(label="Storage")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        content.append(title)

        metrics = get_storage_metrics()
        status, message = describe_storage(metrics)
        content.append(StatusCard(status, message))

        grid = Gtk.Grid(column_spacing=12, row_spacing=12)
        grid.attach(MetricCard("Used", f"{metrics['disk_percent']}%", f"{metrics['disk_used_gb']} GB used"), 0, 0, 1, 1)
        grid.attach(MetricCard("Free", f"{metrics['disk_free_gb']} GB", f"Total: {metrics['disk_total_gb']} GB"), 1, 0, 1, 1)
        content.append(grid)

        content.append(StatusCard("Safety", "pα0.2 does not clean, delete or modify storage. This view is read-only."))
        self.set_child(content)
