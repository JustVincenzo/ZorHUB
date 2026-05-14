import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.core.version import APP_NAME, VERSION, CODENAME, CHANNEL, PUBLIC_RELEASE, STABILITY, MAINTAINER, REPOSITORY_URL, LICENSE_NAME
from app.ui.widgets.status_card import StatusCard


class AboutView(Gtk.ScrolledWindow):
    def __init__(self) -> None:
        super().__init__()
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)

        title = Gtk.Label(label="About ZorHUB")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        content.append(title)

        version_body = (
            f"Version: {VERSION}\n"
            f"Codename: {CODENAME}\n"
            f"Channel: {CHANNEL}\n"
            f"Stability: {STABILITY}\n"
            f"Public release: {'Yes' if PUBLIC_RELEASE else 'No'}"
        )
        content.append(StatusCard(APP_NAME, version_body))
        content.append(StatusCard("License", LICENSE_NAME))
        content.append(StatusCard("Maintainer", f"{MAINTAINER}\nOfficial repository: {REPOSITORY_URL}"))
        content.append(StatusCard("Disclaimer", "ZorHUB is an independent project and is not affiliated with, endorsed by, or maintained by Zorin OS Technologies Ltd."))
        content.append(StatusCard("Private pre-alpha warning", "This build is unstable, incomplete and not intended for public use. Do not use it on critical systems."))

        self.set_child(content)
