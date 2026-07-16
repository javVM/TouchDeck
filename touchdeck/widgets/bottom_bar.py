from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class BottomBar(Gtk.Box):
    """Bottom navigation bar."""

    def __init__(
        self,
        on_home=None,
        on_settings=None,
        on_power=None,
    ) -> None:

        super().__init__(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=20,
        )

        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.add_css_class(
            "bottom-bar"
        )

        self._home = Gtk.Button(
            icon_name="go-home-symbolic"
        )

        self._settings = Gtk.Button(
            icon_name="emblem-system-symbolic"
        )

        self._power = Gtk.Button(
            icon_name="system-shutdown-symbolic"
        )

        self._home.set_hexpand(True)
        self._settings.set_hexpand(True)
        self._power.set_hexpand(True)

        self.append(
            self._home
        )

        self.append(
            self._settings
        )

        self.append(
            self._power
        )

        if on_home:
            self._home.connect(
                "clicked",
                lambda *_: on_home(),
            )

        if on_settings:
            self._settings.connect(
                "clicked",
                lambda *_: on_settings(),
            )

        if on_power:
            self._power.connect(
                "clicked",
                lambda *_: on_power(),
            )