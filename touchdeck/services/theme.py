from __future__ import annotations

from pathlib import Path

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, Gdk


class ThemeService:
    """Manages application themes."""

    def __init__(self) -> None:
        self._styles_path = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "styles"
        )

    def load(
        self,
        theme: str = "dark",
    ) -> None:
        """Load and apply theme."""

        css_file = (
            self._styles_path
            / f"{theme}.css"
        )

        provider = Gtk.CssProvider()

        provider.load_from_path(
            str(css_file)
        )

        display = Gdk.Display.get_default()

        if display:
            Gtk.StyleContext.add_provider_for_display(
                display,
                provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
            )