from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.core.navigation import NavigationStack
from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.services.navigation import NavigationService
from touchdeck.services.settings import SettingsService
from touchdeck.widgets.bottom_bar import BottomBar
from touchdeck.widgets.header import Header


class MainLayout(Gtk.Box):
    """Main application layout."""

    def __init__(self) -> None:
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
        )

        self._config_service = ConfigService()
        self._launcher_service = LauncherService()
        self._navigation_service = NavigationService()
        self._settings_service = SettingsService()

        self._header = Header()

        self._navigation = NavigationStack(
            config_service=self._config_service,
            launcher_service=self._launcher_service,
            navigation_service=self._navigation_service,
            settings_service=self._settings_service,
        )

        self._navigation.set_vexpand(
            True,
        )

        self._bottom_bar = BottomBar(
            navigation_service=self._navigation_service,
        )

        self.append(
            self._header,
        )

        self.append(
            self._navigation,
        )

        self.append(
            self._bottom_bar,
        )