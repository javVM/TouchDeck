from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.models.app_entry import AppEntry
from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.widgets.app_tile import AppTile


class HomePage(Gtk.Box):
    """Main launcher page."""

    def __init__(self) -> None:
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=20,
        )

        self._config = ConfigService()
        self._launcher = LauncherService()

        self._build_ui()

    def _build_ui(self) -> None:
        """Build the page UI."""

        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self._grid = Gtk.Grid(
            row_spacing=20,
            column_spacing=20,
        )

        self._populate_grid()

        self.append(self._grid)

    def _populate_grid(self) -> None:
        """Populate the launcher grid."""

        apps = self._config.load_apps()

        row = 0
        col = 0

        for app in apps:
            tile = AppTile(app)

            tile.connect(
                "activated",
                self._on_app_activated,
            )

            self._grid.attach(
                tile,
                col,
                row,
                1,
                1,
            )

            col += 1

            if col == 2:
                col = 0
                row += 1

    def _on_app_activated(
        self,
        _: AppTile,
        app: AppEntry,
    ) -> None:
        """Launch the selected application."""

        self._launcher.launch(app)