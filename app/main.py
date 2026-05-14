# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw

from app.core.config import ConfigManager
from app.core.errors import ZorHubError
from app.core.history import HistoryManager
from app.core.logger import setup_logger
from app.core.version import APPLICATION_ID
from app.ui.window import ZorHubWindow


class ZorHubApplication(Adw.Application):
    def __init__(self) -> None:
        super().__init__(application_id=APPLICATION_ID)
        self.logger = setup_logger()
        self.config = ConfigManager()
        self.history = HistoryManager()

    def do_activate(self) -> None:
        self.logger.info("Activating ZorHUB window")
        self.history.add_event("app.start", "ZorHUB application window activated.")
        window = ZorHubWindow(self, self.config, self.history)
        window.present()


def main() -> int:
    try:
        app = ZorHubApplication()
        return app.run(sys.argv)
    except ZorHubError as exc:
        print(f"ZorHUB error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
