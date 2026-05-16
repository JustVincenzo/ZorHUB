# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

from typing import Callable

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from app.core.config import ConfigManager


class OnboardingView(Gtk.ScrolledWindow):
    """
    Initial onboarding view for ZorHUB pα0.2.1-dev.

    This screen is not decorative. It informs the user about what ZorHUB is,
    what it can and cannot do in this version, and asks for background
    behavior preference.
    """

    def __init__(self, config: ConfigManager, on_finish: Callable[[], None]) -> None:
        super().__init__()

        self.config = config
        self.on_finish = on_finish

        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_hexpand(True)
        self.set_vexpand(True)

        self._build_ui()

    def _build_ui(self) -> None:
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=18)
        content.set_margin_top(32)
        content.set_margin_bottom(32)
        content.set_margin_start(32)
        content.set_margin_end(32)
        content.set_hexpand(True)
        content.set_vexpand(False)

        title = Gtk.Label(label="Welcome to ZorHUB")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        subtitle = Gtk.Label(
            label=(
                "ZorHUB is a private pre-alpha system hub for Ubuntu-based Linux "
                "distributions. This onboarding explains what the app does, what it "
                "does not do yet, and asks how background behavior should be handled."
            )
        )
        subtitle.add_css_class("dim-label")
        subtitle.set_halign(Gtk.Align.START)
        subtitle.set_xalign(0)
        subtitle.set_wrap(True)
        content.append(subtitle)

        content.append(self._create_intro_group())
        content.append(self._create_safety_group())
        content.append(self._create_background_group())
        content.append(self._create_agent_group())
        content.append(self._create_user_choice_group())

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        button_box.set_halign(Gtk.Align.START)
        button_box.set_hexpand(True)

        continue_without_background = Gtk.Button(label="Continue without background")
        continue_without_background.connect("clicked", self._continue_without_background)

        allow_background = Gtk.Button(label="Allow background preference")
        allow_background.add_css_class("suggested-action")
        allow_background.connect("clicked", self._continue_with_background)

        button_box.append(continue_without_background)
        button_box.append(allow_background)

        content.append(button_box)

        clamp = Adw.Clamp()
        clamp.set_maximum_size(820)
        clamp.set_tightening_threshold(500)
        clamp.set_child(content)

        self.set_child(clamp)

    def _create_intro_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup()
        group.set_title("What ZorHUB is")

        row = Adw.ExpanderRow()
        row.set_title("ZorHUB is a visual system hub")
        row.set_subtitle("It explains system information in a clear and human-readable way.")

        row.add_row(
            self._create_info_row(
                "Purpose",
                (
                    "ZorHUB is designed to unify fragmented system tasks through a simple "
                    "visual interface. It is not meant to be only a technical system monitor."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "Current version",
                (
                    "This is pα0.2.1-dev, a private pre-alpha development build. "
                    "It is incomplete, unstable, and not intended for public release."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "Platform focus",
                (
                    "The first target platform family is Ubuntu-based Linux distributions, "
                    "with Zorin OS as the primary design reference."
                ),
            )
        )

        group.add(row)
        return group

    def _create_safety_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup()
        group.set_title("Safety boundary")

        row = Adw.ExpanderRow()
        row.set_title("ZorHUB will not modify your system in this version")
        row.set_subtitle("pα0.2.1-dev is read-only except for local app settings and logs.")

        row.add_row(
            self._create_info_row(
                "No system modification",
                (
                    "ZorHUB pα0.2.1-dev does not install applications, remove packages, "
                    "repair package managers, clean system files, manage services, or modify "
                    "system configuration."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "No privileged commands",
                (
                    "This version does not use sudo, pkexec, Polkit, or any privileged "
                    "system authorization flow."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "What it can write",
                (
                    "ZorHUB may write local application configuration, local logs, and local "
                    "history files inside user-level directories."
                ),
            )
        )

        group.add(row)
        return group

    def _create_background_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup()
        group.set_title("Background behavior")

        row = Adw.ExpanderRow()
        row.set_title("Choose how ZorHUB should handle background behavior")
        row.set_subtitle("No real background service is active in pα0.2.1-dev.")

        row.add_row(
            self._create_info_row(
                "Current behavior",
                (
                    "In this version, ZorHUB only stores your background preference. "
                    "It does not start a background daemon, background service, or hidden "
                    "system process."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "Future behavior",
                (
                    "Future versions may use background behavior for safe tasks such as "
                    "component status checks, reminders, or non-privileged notifications. "
                    "System-changing actions must still require explanation, confirmation, "
                    "and authorization."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "Your choice",
                (
                    "You can continue without allowing background behavior, or allow ZorHUB "
                    "to store a preference for future background features."
                ),
            )
        )

        group.add(row)
        return group

    def _create_agent_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup()
        group.set_title("ZorHUB Agent")

        row = Adw.ExpanderRow()
        row.set_title("ZorHUB Agent is not available yet")
        row.set_subtitle("Agent, D-Bus and Polkit are planned for later versions.")

        row.add_row(
            self._create_info_row(
                "No Agent in this version",
                (
                    "ZorHUB Agent does not exist in pα0.2.1-dev. The current app cannot "
                    "perform advanced system actions through Agent."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "No D-Bus communication",
                (
                    "This version does not communicate with any Agent through D-Bus. "
                    "The Main ↔ Agent communication model will be planned in pα0.3."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "Future role of Agent",
                (
                    "In future versions, ZorHUB Agent will be a separate Rust-based native "
                    "component responsible for authorized advanced actions."
                ),
            )
        )

        group.add(row)
        return group

    def _create_user_choice_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup()
        group.set_title("Before continuing")

        row = Adw.ExpanderRow()
        row.set_title("Your confirmation")
        row.set_subtitle("Read this before entering ZorHUB.")

        row.add_row(
            self._create_info_row(
                "What you are allowing",
                (
                    "By continuing, you are only allowing ZorHUB to open its interface and "
                    "store local preferences. You are not allowing system modification."
                ),
            )
        )

        row.add_row(
            self._create_info_row(
                "What you are not allowing",
                (
                    "You are not allowing package installation, system repair, privileged "
                    "actions, background system modification, or Agent-based operations."
                ),
            )
        )

        group.add(row)
        return group

    def _create_info_row(self, title: str, body: str) -> Adw.ActionRow:
        row = Adw.ActionRow()
        row.set_title(title)
        row.set_subtitle(body)
        row.set_subtitle_lines(8)
        return row

    def _continue_without_background(self, _button: Gtk.Button) -> None:
        self.config.set("background_allowed", False)
        self.config.set("first_run", False)
        self.on_finish()

    def _continue_with_background(self, _button: Gtk.Button) -> None:
        self.config.set("background_allowed", True)
        self.config.set("first_run", False)
        self.on_finish()
