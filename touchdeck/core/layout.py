from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.core.navigation import NavigationStack


class MainLayout(Gtk.Box):
    """Main application layout."""

    def __init__(self) -> None:

        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
        )

        self._navigation = NavigationStack()

        self.append(
            self._navigation
        )