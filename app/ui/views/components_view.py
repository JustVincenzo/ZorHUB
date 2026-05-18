# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from app.core.config import ConfigManager
from app.core.history import HistoryManager
from app.services.component_service import ComponentService
from app.ui.widgets.component_card import ComponentCard
from app.ui.widgets.status_card import StatusCard


class ComponentsView(Gtk.ScrolledWindow):
    def __init__(self, config: ConfigManager, history: HistoryManager) -> None:
        super().__init__()

        self.config = config
        self.history = history
        self.component_service = ComponentService(config)

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

        title = Gtk.Label(label="Components")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        subtitle = Gtk.Label(
            label=(
                "Components are internal ZorHUB capabilities, not separate public apps. "
                "In pα0.2.1-dev, enabling or disabling a component only saves a local "
                "preference. It does not install, remove, start, stop, or modify anything "
                "in the system."
            )
        )
        subtitle.add_css_class("dim-label")
        subtitle.set_halign(Gtk.Align.START)
        subtitle.set_xalign(0)
        subtitle.set_wrap(True)
        content.append(subtitle)

        content.append(
            StatusCard(
                "Safety boundary",
                (
                    "ZorHUB Agent does not exist in this version.\n"
                    "D-Bus communication is not implemented in this version.\n"
                    "Polkit authorization is not implemented in this version.\n\n"
                    "Component switches only change local ZorHUB preferences."
                ),
            )
        )

        for component in self.component_service.list_components():
            content.append(
                ComponentCard(
                    component=component,
                    config=self.config,
                    on_component_toggled=self._on_component_toggled,
                )
            )

        self.set_child(content)

    def _on_component_toggled(self, component: dict, enabled: bool) -> None:
        component_id = component.get("id", "unknown")
        component_name = component.get("name", component_id)

        event_type = "component.enabled" if enabled else "component.disabled"
        message = (
            f"Component enabled: {component_name}"
            if enabled
            else f"Component disabled: {component_name}"
        )

        self.history.add_event(
            event_type=event_type,
            message=message,
            details={
                "component_id": component_id,
                "component_name": component_name,
                "enabled": enabled,
                "system_action_performed": False,
                "agent_required": bool(component.get("requires_agent", False)),
                "agent_available": False,
            },
        )
