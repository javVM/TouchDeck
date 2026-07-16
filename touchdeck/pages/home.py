from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.widgets.app_grid import AppGrid


class HomePage(Gtk.Box):
    """Main launcher page."""

    def __init__(
        self,
        config_service: ConfigService,
        launcher_service: LauncherService,
    ) -> None:
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
        )

        self.set_hexpand(True)
        self.set_vexpand(True)

        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.append(
            AppGrid(
                config_service=config_service,
                launcher_service=launcher_service,
            )
        )