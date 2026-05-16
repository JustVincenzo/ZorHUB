# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vynzaro
#
# This file is part of ZorHUB.

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from app.core.version import (
    APP_NAME,
    VERSION,
    CODENAME,
    CHANNEL,
    PUBLIC_RELEASE,
    STABILITY,
    MAINTAINER,
    REPOSITORY_URL,
    LICENSE_NAME,
)
from app.ui.widgets.status_card import StatusCard


class AboutView(Gtk.ScrolledWindow):
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

        title = Gtk.Label(label="About ZorHUB")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        subtitle = Gtk.Label(
            label=(
                "ZorHUB is a private pre-alpha visual system hub for Ubuntu-based "
                "Linux distributions. This build is intended for internal development "
                "and testing only."
            )
        )
        subtitle.add_css_class("dim-label")
        subtitle.set_halign(Gtk.Align.START)
        subtitle.set_xalign(0)
        subtitle.set_wrap(True)
        content.append(subtitle)

        version_body = (
            f"Version: {VERSION}\n"
            f"Codename: {CODENAME}\n"
            f"Channel: {CHANNEL}\n"
            f"Stability: {STABILITY}\n"
            f"Public release: {'Yes' if PUBLIC_RELEASE else 'No'}"
        )

        content.append(StatusCard(APP_NAME, version_body))

        content.append(
            StatusCard(
                "License",
                (
                    f"{LICENSE_NAME}\n\n"
                    "ZorHUB is currently licensed under GPL-3.0-or-later. "
                    "See the LICENSE file in the project repository for the full license text."
                ),
            )
        )

        content.append(
            StatusCard(
                "Maintainer",
                (
                    f"{MAINTAINER}\n\n"
                    f"Official repository:\n{REPOSITORY_URL}"
                ),
            )
        )

        content.append(
            StatusCard(
                "Pre-alpha warning",
                (
                    "This build is unstable, incomplete, and not intended for public use.\n\n"
                    "Do not use it on critical systems. ZorHUB pα0.2.1-dev may read basic "
                    "system information and write local configuration, logs, and history, "
                    "but it must not modify system files or perform privileged actions."
                ),
            )
        )

        content.append(
            StatusCard(
                "Safety boundary",
                (
                    "No ZorHUB Agent is implemented in this version.\n"
                    "No D-Bus communication is implemented in this version.\n"
                    "No Polkit authorization is implemented in this version.\n"
                    "No package installation, package removal, package repair, service "
                    "management, or system cleanup is implemented in this version."
                ),
            )
        )

        content.append(
            StatusCard(
                "Disclaimer",
                (
                    "ZorHUB is an independent project and is not affiliated with, "
                    "endorsed by, sponsored by, or maintained by Zorin OS Technologies Ltd.\n\n"
                    "Zorin OS, Zorin, and related marks are property of their respective owners. "
                    "References to Zorin OS are descriptive and do not imply endorsement."
                ),
            )
        )

        self.set_child(content)
