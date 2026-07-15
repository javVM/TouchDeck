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
        """Build page layout."""

        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self._apps_box = Gtk.FlowBox(
            homogeneous=True,
            row_spacing=20,
            column_spacing=20,
            selection_mode=Gtk.SelectionMode.NONE,
        )

        self._apps_box.set_valign(
            Gtk.Align.START
        )

        self._populate_apps()

        self.append(self._apps_box)

    def _populate_apps(self) -> None:
        """Load applications and create tiles."""

        apps = self._config.load_apps()

        for app in apps:

            tile = AppTile(app)

            tile.connect(
                "activated",
                self._on_app_activated,
            )

            self._apps_box.insert(
                tile,
                -1,
            )

    def _on_app_activated(
        self,
        _: AppTile,
        app: AppEntry,
    ) -> None:
        """Launch selected application."""

        self._launcher.launch(app)