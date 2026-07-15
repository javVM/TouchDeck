from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk, Gdk

from touchdeck.core.window import MainWindow


class TouchDeckApplication(Adw.Application):
    """Main TouchDeck application."""

    def __init__(self) -> None:
        super().__init__(
            application_id="io.touchdeck.TouchDeck"
        )

    def do_startup(self) -> None:
        """Application startup."""

        Adw.Application.do_startup(self)

        self._load_css()

    def do_activate(self) -> None:
        """Activate application."""

        window = self.props.active_window

        if not window:
            window = MainWindow(
                application=self
            )

        window.present()

    def _load_css(self) -> None:
        """Load application CSS."""

        provider = Gtk.CssProvider()

        provider.load_from_path(
            "styles/base.css"
        )

        display = Gdk.Display.get_default()

        if display:
            Gtk.StyleContext.add_provider_for_display(
                display,
                provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
            )