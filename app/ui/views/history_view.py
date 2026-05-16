# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.core.history import HistoryManager
from app.ui.widgets.status_card import StatusCard


class HistoryView(Gtk.ScrolledWindow):
    def __init__(self, history: HistoryManager) -> None:
        super().__init__()

        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_hexpand(True)
        self.set_vexpand(True)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)
        content.set_hexpand(True)
        content.set_vexpand(False)

        title = Gtk.Label(label="History")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        subtitle = Gtk.Label(
            label=(
                "History shows local ZorHUB events. In pα0.2.1-dev, this only covers "
                "local app activity and does not include privileged system actions."
            )
        )
        subtitle.add_css_class("dim-label")
        subtitle.set_halign(Gtk.Align.START)
        subtitle.set_xalign(0)
        subtitle.set_wrap(True)
        content.append(subtitle)

        events = history.read_events(limit=50)

        if not events:
            content.append(StatusCard("No events", "ZorHUB has not recorded local events yet."))
        else:
            for event in reversed(events):
                body = f"{event.get('timestamp', '')}\n{event.get('message', '')}"
                content.append(StatusCard(event.get("type", "event"), body))

        self.set_child(content)
