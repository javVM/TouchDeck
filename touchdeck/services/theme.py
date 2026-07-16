from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from pathlib import Path

from gi.repository import Gdk, Gtk

from touchdeck.enums.theme import Theme
from touchdeck.services.settings import SettingsService


class ThemeService:
    """Manage application themes."""

    def __init__(
        self,
        settings_service: SettingsService,
    ) -> None:

        self._settings_service = settings_service

        self._provider = Gtk.CssProvider()

        self._styles_path = (
            Path(__file__).resolve()
            .parent.parent
            / "styles"
        )

    def apply(self) -> None:
        """Apply the current application theme."""

        theme = self._settings_service.settings.theme

        css_file = self._styles_path / f"{theme.value}.css"

        self._provider.load_from_path(
            str(css_file),
        )

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            self._provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )