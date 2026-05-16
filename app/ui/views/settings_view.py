# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

from app.core.config import ConfigManager
from app.core.paths import LOG_DIR


class SettingsView(Gtk.ScrolledWindow):
    def __init__(self, config: ConfigManager) -> None:
        super().__init__()

        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_hexpand(True)
        self.set_vexpand(True)

        self.config = config

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)
        content.set_hexpand(True)
        content.set_vexpand(False)

        title = Gtk.Label(label="Settings")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        content.append(self._appearance_group())
        content.append(self._mode_group())
        content.append(self._background_group())
        content.append(self._logs_group())

        self.set_child(content)

    def _appearance_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup(title="Appearance")
        combo = Gtk.ComboBoxText()
        combo.append("system", "Follow system")
        combo.append("light", "Light")
        combo.append("dark", "Dark")
        combo.set_active_id(self.config.get("appearance", "system"))
        combo.connect("changed", self._on_appearance_changed)row = Adw.ActionRow()
        row.set_title("Theme mode")
        row.set_subtitle("Default: follow system appearance")
        row.add_suffix(combo)
        group.add(row)
        return group

    def _mode_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup(title="User mode")
        combo = Gtk.ComboBoxText()
        combo.append("simple", "Simple")
        combo.append("advanced", "Advanced")
        combo.set_active_id(self.config.get("user_mode", "simple"))
        combo.connect("changed", self._on_user_mode_changed)
        row = Adw.ActionRow()
        row.set_title("Information level")
        row.set_subtitle("Advanced mode may show technical details")
        row.add_suffix(combo)
        group.add(row)
        return group

    def _background_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup(title="Background")
        switch = Gtk.Switch()
        switch.set_active(bool(self.config.get("background_allowed", False)))
        switch.connect("notify::active", self._on_background_changed)
        row = Adw.ActionRow()
        row.set_title("Allow background behavior")
        row.set_subtitle("pα0.2.1-dev stores consent only. No background service is active yet.")
        row.set_subtitle_lines(3)
        row.add_suffix(switch)
        group.add(row)
        return group

    def _logs_group(self) -> Adw.PreferencesGroup:
        group = Adw.PreferencesGroup(title="Logs")
        row = Adw.ActionRow()
        row.set_title("Log location")
        row.set_subtitle(str(LOG_DIR))
        row.set_subtitle_lines(3)
        group.add(row)
        return group

    def _on_appearance_changed(self, combo: Gtk.ComboBoxText) -> None:
        active_id = combo.get_active_id() or "system"
        self.config.set("appearance", active_id)
        style_manager = Adw.StyleManager.get_default()
        if active_id == "system":
            style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)
        elif active_id == "light":
            style_manager.set_color_scheme(Adw.ColorScheme.FORCE_LIGHT)
        elif active_id == "dark":
            style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

    def _on_user_mode_changed(self, combo: Gtk.ComboBoxText) -> None:
        self.config.set("user_mode", combo.get_active_id() or "simple")

    def _on_background_changed(self, switch: Gtk.Switch, _param) -> None:
        self.config.set("background_allowed", switch.get_active())
