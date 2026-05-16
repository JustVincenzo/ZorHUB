# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.core.config import ConfigManager
from app.services.component_service import ComponentService
from app.ui.widgets.component_card import ComponentCard


class ComponentsView(Gtk.ScrolledWindow):
    def __init__(self, config: ConfigManager) -> None:
        super().__init__()
        self.config = config
        self.component_service = ComponentService(config)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)

        title = Gtk.Label(label="Components")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        content.append(title)

        subtitle = Gtk.Label(label="Components are ZorHUB capabilities, not separate public apps. pα0.2 only detects and explains them.")
        subtitle.set_wrap(True)
        subtitle.add_css_class("dim-label")
        subtitle.set_halign(Gtk.Align.START)
        content.append(subtitle)

        for component in self.component_service.list_components():
            content.append(ComponentCard(component))

        self.set_child(content)
