from __future__ import annotations

import gi

gi.require_version("Adw", "1")

from gi.repository import Adw

from touchdeck.core.services import Services
from touchdeck.core.window import MainWindow


class TouchDeckApplication(Adw.Application):
    """Main TouchDeck application."""

    def __init__(self) -> None:
        super().__init__(
            application_id="io.touchdeck.TouchDeck",
        )

        self._services = Services()

    def do_startup(self) -> None:
        """Application startup."""

        Adw.Application.do_startup(self)

        self._services.theme.apply()

    def do_activate(self) -> None:
        """Activate application."""

        window = self.props.active_window

        if not window:
            window = MainWindow(
                application=self,
                services=self._services,
            )

        window.present()