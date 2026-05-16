# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class MetricCard(Gtk.Box):
    def __init__(self, label: str, value: str, detail: str = "") -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        self.add_css_class("card")
        self.set_hexpand(True)
        self.set_vexpand(False)
        self.set_margin_top(6)
        self.set_margin_bottom(6)
        self.set_margin_start(6)
        self.set_margin_end(6)

        inner = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        inner.set_hexpand(True)
        inner.set_vexpand(False)
        inner.set_margin_top(14)
        inner.set_margin_bottom(14)
        inner.set_margin_start(14)
        inner.set_margin_end(14)

        label_widget = Gtk.Label(label=label)
        label_widget.add_css_class("caption")
        label_widget.set_halign(Gtk.Align.START)
        label_widget.set_xalign(0)
        label_widget.set_wrap(True)

        value_widget = Gtk.Label(label=value)
        value_widget.add_css_class("title-2")
        value_widget.set_halign(Gtk.Align.START)
        value_widget.set_xalign(0)
        value_widget.set_wrap(True)

        inner.append(label_widget)
        inner.append(value_widget)

        if detail:
            detail_widget = Gtk.Label(label=detail)
            detail_widget.add_css_class("dim-label")
            detail_widget.set_halign(Gtk.Align.START)
            detail_widget.set_xalign(0)
            detail_widget.set_wrap(True)
            inner.append(detail_widget)

        self.append(inner)
