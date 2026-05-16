# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class StatusCard(Gtk.Box):
    def __init__(self, title: str, body: str) -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        self.add_css_class("card")
        self.set_hexpand(True)
        self.set_vexpand(False)
        self.set_margin_top(6)
        self.set_margin_bottom(6)
        self.set_margin_start(6)
        self.set_margin_end(6)

        inner = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        inner.set_hexpand(True)
        inner.set_vexpand(False)
        inner.set_margin_top(16)
        inner.set_margin_bottom(16)
        inner.set_margin_start(16)
        inner.set_margin_end(16)

        title_label = Gtk.Label(label=title)
        title_label.add_css_class("title-3")
        title_label.set_halign(Gtk.Align.START)
        title_label.set_xalign(0)
        title_label.set_wrap(True)

        body_label = Gtk.Label(label=body)
        body_label.set_halign(Gtk.Align.START)
        body_label.set_xalign(0)
        body_label.set_wrap(True)
        body_label.set_selectable(True)

        inner.append(title_label)
        inner.append(body_label)

        self.append(inner)
