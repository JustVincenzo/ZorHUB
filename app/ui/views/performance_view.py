# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app.services.performance_service import get_performance_metrics, describe_performance
from app.ui.widgets.status_card import StatusCard
from app.ui.widgets.metric_card import MetricCard


class PerformanceView(Gtk.ScrolledWindow):
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

        title = Gtk.Label(label="Performance")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        metrics = get_performance_metrics()
        status, message = describe_performance(metrics)

        content.append(StatusCard(f"Performance: {status}", message))

        grid = Gtk.Grid(column_spacing=12, row_spacing=12)
        grid.set_hexpand(True)
        grid.set_column_homogeneous(True)

        grid.attach(MetricCard("CPU", f"{metrics['cpu_percent']}%"), 0, 0, 1, 1)
        grid.attach(
            MetricCard(
                "RAM",
                f"{metrics['ram_percent']}%",
                f"{metrics['ram_used_gb']} GB / {metrics['ram_total_gb']} GB",
            ),
            1,
            0,
            1,
            1,
        )
        grid.attach(MetricCard("Swap", f"{metrics['swap_percent']}%"), 0, 1, 1, 1)
        grid.attach(MetricCard("Processes", str(metrics["process_count"])), 1, 1, 1, 1)

        content.append(grid)

        self.set_child(content)
