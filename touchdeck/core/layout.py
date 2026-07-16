from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.core.navigation import NavigationStack
from touchdeck.core.services import Services
from touchdeck.widgets.bottom_bar import BottomBar
from touchdeck.widgets.header import Header


class MainLayout(Gtk.Box):
    """Main application layout."""

    def __init__(
        self,
        services: Services,
    ) -> None:
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
        )

        self._services = services

        self._header = Header()

        self._navigation = NavigationStack(
            services,
        )

        self._navigation.set_vexpand(
            True,
        )

        self._bottom_bar = BottomBar(
            navigation_service=self._services.navigation,
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