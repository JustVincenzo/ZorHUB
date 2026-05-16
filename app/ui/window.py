# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from app.core.config import ConfigManager
from app.core.history import HistoryManager
from app.core.version import APP_NAME

from app.ui.views.home_view import HomeView
from app.ui.views.performance_view import PerformanceView
from app.ui.views.storage_view import StorageView
from app.ui.views.components_view import ComponentsView
from app.ui.views.settings_view import SettingsView
from app.ui.views.about_view import AboutView
from app.ui.views.onboarding_view import OnboardingView
from app.ui.views.history_view import HistoryView


class ZorHubWindow(Adw.ApplicationWindow):
    def __init__(self, app: Adw.Application, config: ConfigManager, history: HistoryManager) -> None:
        super().__init__(application=app)

        self.config = config
        self.history = history

        self.set_title(APP_NAME)
        self.set_default_size(1100, 700)
        self.set_size_request(900, 560)

        self._build_ui()

    def _build_ui(self) -> None:
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.main_box.set_hexpand(True)
        self.main_box.set_vexpand(True)

        self.header = Adw.HeaderBar()
        self.main_box.append(self.header)

        self.content_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.content_area.set_hexpand(True)
        self.content_area.set_vexpand(True)

        self.main_box.append(self.content_area)

        self.set_content(self.main_box)

        if self.config.get("first_run", True):
            self._show_onboarding()
        else:
            self._show_main_interface()

    def _clear_content_area(self) -> None:
        child = self.content_area.get_first_child()

        while child is not None:
            next_child = child.get_next_sibling()
            self.content_area.remove(child)
            child = next_child

    def _show_onboarding(self) -> None:
        self._clear_content_area()

        onboarding = OnboardingView(self.config, self._show_main_interface)
        onboarding.set_hexpand(True)
        onboarding.set_vexpand(True)

        self.content_area.append(onboarding)

    def _show_main_interface(self) -> None:
        self._clear_content_area()
        self._append_main_interface()

    def _append_main_interface(self) -> None:
        paned = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        paned.set_wide_handle(False)
        paned.set_position(220)
        paned.set_hexpand(True)
        paned.set_vexpand(True)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.stack.set_hexpand(True)
        self.stack.set_vexpand(True)

        self.stack.add_titled(HomeView(), "home", "Home")
        self.stack.add_titled(PerformanceView(), "performance", "Performance")
        self.stack.add_titled(StorageView(), "storage", "Storage")
        self.stack.add_titled(ComponentsView(self.config), "components", "Components")
        self.stack.add_titled(HistoryView(self.history), "history", "History")
        self.stack.add_titled(SettingsView(self.config), "settings", "Settings")
        self.stack.add_titled(AboutView(), "about", "About")

        sidebar = Gtk.StackSidebar(stack=self.stack)
        sidebar.set_size_request(220, -1)
        sidebar.set_vexpand(True)
        sidebar.set_margin_top(12)
        sidebar.set_margin_bottom(12)
        sidebar.set_margin_start(12)
        sidebar.set_margin_end(12)

        paned.set_start_child(sidebar)
        paned.set_end_child(self.stack)

        self.content_area.append(paned)
