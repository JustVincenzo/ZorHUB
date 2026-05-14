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
        self._build_ui()

    def _build_ui(self) -> None:
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.header = Adw.HeaderBar()
        self.main_box.append(self.header)

        if self.config.get("first_run", True):
            self.main_box.append(OnboardingView(self.config, self._show_main_interface))
        else:
            self._append_main_interface()

        self.set_content(self.main_box)

    def _show_main_interface(self) -> None:
        child = self.main_box.get_last_child()
        if child:
            self.main_box.remove(child)
        self._append_main_interface()

    def _append_main_interface(self) -> None:
        paned = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        paned.set_wide_handle(False)
        paned.set_position(220)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)

        self.stack.add_titled(HomeView(), "home", "Home")
        self.stack.add_titled(PerformanceView(), "performance", "Performance")
        self.stack.add_titled(StorageView(), "storage", "Storage")
        self.stack.add_titled(ComponentsView(self.config), "components", "Components")
        self.stack.add_titled(HistoryView(self.history), "history", "History")
        self.stack.add_titled(SettingsView(self.config), "settings", "Settings")
        self.stack.add_titled(AboutView(), "about", "About")

        sidebar = Gtk.StackSidebar(stack=self.stack)
        sidebar.set_margin_top(12)
        sidebar.set_margin_bottom(12)
        sidebar.set_margin_start(12)
        sidebar.set_margin_end(12)

        paned.set_start_child(sidebar)
        paned.set_end_child(self.stack)
        self.main_box.append(paned)
