from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.core.navigation import NavigationStack
from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.widgets.bottom_bar import BottomBar
from touchdeck.widgets.header import Header


class MainLayout(Gtk.Box):
    """Main application layout."""

    def __init__(self) -> None:
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
        )

        self._config = ConfigService()
        self._launcher = LauncherService()

        self._header = Header()

        self._navigation = NavigationStack(
            config_service=self._config,
            launcher_service=self._launcher,
        )

        self._navigation.set_vexpand(
            True,
        )

        self._bottom_bar = BottomBar()

        self.append(
            self._header,
        )

        self.append(
            self._navigation,
        )

        self.append(
            self._bottom_bar,
        )