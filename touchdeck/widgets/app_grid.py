from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.models.app_entry import AppEntry
from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.widgets.app_tile import AppTile


class AppGrid(Gtk.ScrolledWindow):
    """Grid displaying launchable applications."""

    def __init__(
        self,
        config_service: ConfigService,
        launcher_service: LauncherService,
    ) -> None:
        super().__init__()

        self.set_hexpand(True)
        self.set_vexpand(True)

        self._config = config_service
        self._launcher = launcher_service

        self._flowbox = Gtk.FlowBox(
            homogeneous=True,
            row_spacing=20,
            column_spacing=20,
            selection_mode=Gtk.SelectionMode.NONE,
        )

        self._flowbox.set_valign(
            Gtk.Align.START,
        )

        self.set_child(
            self._flowbox,
        )

        self._load_apps()

    def _load_apps(self) -> None:
        """Load configured applications."""

        apps = self._config.load_apps()

        for app in apps:
            tile = self._create_tile(app)

            self._flowbox.insert(
                tile,
                -1,
            )

    def _create_tile(
        self,
        app: AppEntry,
    ) -> AppTile:
        """Create an application tile."""

        tile = AppTile(app)

        tile.connect(
            "activated",
            self._on_app_activated,
        )

        return tile

    def _on_app_activated(
        self,
        _: AppTile,
        app: AppEntry,
    ) -> None:
        """Launch selected application."""

        self._launcher.launch(app)