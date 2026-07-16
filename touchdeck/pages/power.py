from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class PowerPage(Gtk.Box):
    """Power management page."""

    def __init__(self) -> None:
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=20,
        )

        self.set_hexpand(True)
        self.set_vexpand(True)

        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)

        title = Gtk.Label(
            label="Power",
            xalign=0,
        )

        title.add_css_class(
            "title-1",
        )

        self.append(
            title,
        )

        self.append(
            Gtk.Separator(
                orientation=Gtk.Orientation.HORIZONTAL,
            ),
        )

        self.append(
            Gtk.Button(
                label="Lock Screen",
            ),
        )

        self.append(
            Gtk.Button(
                label="Restart",
            ),
        )

        self.append(
            Gtk.Button(
                label="Shutdown",
            ),
        )