# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class StorageView(Gtk.ScrolledWindow):
    def __init__(self) -> None:
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

        title = Gtk.Label(label="Storage")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        metrics = get_storage_metrics()
        status, message = describe_storage(metrics)

        content.append(StatusCard(status, message))

        grid = Gtk.Grid(column_spacing=12, row_spacing=12)
        grid.set_hexpand(True)
        grid.set_column_homogeneous(True)

        grid.attach(
            MetricCard(
                "Used",
                f"{metrics['disk_percent']}%",
                f"{metrics['disk_used_gb']} GB used",
            ),
            0,
            0,
            1,
            1,
        )
        grid.attach(
            MetricCard(
                "Free",
                f"{metrics['disk_free_gb']} GB",
                f"Total: {metrics['disk_total_gb']} GB",
            ),
            1,
            0,
            1,
            1,
        )

        content.append(grid)

        content.append(
            StatusCard(
                "Safety",
                "pα0.2.1-dev does not clean, delete, or modify storage. This view is read-only.",
            )
        )

        self.set_child(content)
