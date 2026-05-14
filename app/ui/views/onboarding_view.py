import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.core.config import ConfigManager
from app.ui.widgets.status_card import StatusCard


class OnboardingView(Gtk.ScrolledWindow):
    def __init__(self, config: ConfigManager, on_finish) -> None:
        super().__init__()
        self.config = config
        self.on_finish = on_finish

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)

        title = Gtk.Label(label="Welcome to ZorHUB")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        content.append(title)

        content.append(StatusCard("Private pre-alpha", "This version is incomplete and private. It reads and explains basic system status, but it does not modify the system."))
        content.append(StatusCard("Safety", "ZorHUB will not install apps, repair packages, use sudo, use pkexec or communicate with a real Agent in pα0.2."))
        content.append(StatusCard("Background consent", "You can allow or deny background behavior in Settings. pα0.2 stores this preference only; no background service is active yet."))

        button = Gtk.Button(label="Continue")
        button.add_css_class("suggested-action")
        button.set_halign(Gtk.Align.START)
        button.connect("clicked", self._finish)
        content.append(button)

        self.set_child(content)

    def _finish(self, _button) -> None:
        self.config.set("first_run", False)
        self.on_finish()
