import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.core.history import HistoryManager
from app.ui.widgets.status_card import StatusCard


class HistoryView(Gtk.ScrolledWindow):
    def __init__(self, history: HistoryManager) -> None:
        super().__init__()
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)

        title = Gtk.Label(label="History")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        content.append(title)

        events = history.read_events(limit=50)
        if not events:
            content.append(StatusCard("No events", "ZorHUB has not recorded local events yet."))
        else:
            for event in reversed(events):
                body = f"{event.get('timestamp', '')}\n{event.get('message', '')}"
                content.append(StatusCard(event.get("type", "event"), body))

        self.set_child(content)
