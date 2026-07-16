from __future__ import annotations

import gi

gi.require_version("Adw", "1")

from gi.repository import Adw

from touchdeck.core.layout import MainLayout
from touchdeck.core.services import Services


class MainWindow(Adw.ApplicationWindow):
    """Main application window."""

    def __init__(
        self,
        application: Adw.Application,
        services: Services,
    ) -> None:
        super().__init__(
            application=application,
        )

        self.set_title("TouchDeck")

        self.fullscreen()

        self.set_content(
            MainLayout(services)
        )