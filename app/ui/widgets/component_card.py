# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ComponentCard(Gtk.Box):
    def __init__(self, component: dict) -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add_css_class("card")
        self.set_margin_top(6)
        self.set_margin_bottom(6)
        self.set_margin_start(6)
        self.set_margin_end(6)

        inner = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        inner.set_margin_top(14)
        inner.set_margin_bottom(14)
        inner.set_margin_start(14)
        inner.set_margin_end(14)

        title = Gtk.Label(label=component.get("name", "Unknown component"))
        title.add_css_class("title-3")
        title.set_halign(Gtk.Align.START)

        description = Gtk.Label(label=component.get("description", ""))
        description.set_wrap(True)
        description.set_halign(Gtk.Align.START)

        status = component.get("status", "unknown")
        risk = component.get("risk", "unknown")
        enabled = "Enabled" if component.get("enabled") else "Disabled"
        meta = Gtk.Label(label=f"Status: {status} · Risk: {risk} · {enabled}")
        meta.add_css_class("dim-label")
        meta.set_halign(Gtk.Align.START)

        inner.append(title)
        inner.append(description)
        inner.append(meta)
        self.append(inner)
