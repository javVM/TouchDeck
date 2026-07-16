from __future__ import annotations

from datetime import datetime

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk


class Header(Gtk.Box):
    """Application header."""

    def __init__(self) -> None:
        super().__init__(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=12,
        )

        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.add_css_class("header")

        self._build_ui()

        self._update_clock()

        GLib.timeout_add_seconds(
            1,
            self._update_clock,
        )

    def _build_ui(self) -> None:
        """Build widget hierarchy."""

        self._title = Gtk.Label(
            label="TouchDeck",
            hexpand=True,
            xalign=0,
        )

        self._title.add_css_class(
            "header-title"
        )

        self._clock = Gtk.Label()

        self._clock.add_css_class(
            "header-clock"
        )

        self.append(
            self._title
        )

        self.append(
            self._clock
        )

    def _update_clock(self) -> bool:
        """Refresh clock."""

        self._clock.set_text(
            datetime.now().strftime("%H:%M")
        )

        return True

    def set_title(
        self,
        title: str,
    ) -> None:
        """Set current page title."""

        self._title.set_text(
            title
        )