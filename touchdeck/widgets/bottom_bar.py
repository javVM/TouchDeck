from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.enums.page import Page
from touchdeck.services.navigation import NavigationService


class BottomBar(Gtk.Box):
    """Bottom navigation bar."""

    def __init__(
        self,
        navigation_service: NavigationService,
    ) -> None:
        super().__init__(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=20,
        )

        self._navigation_service = navigation_service

        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.add_css_class(
            "bottom-bar",
        )

        self._home = Gtk.Button(
            icon_name="go-home-symbolic",
        )

        self._settings = Gtk.Button(
            icon_name="emblem-system-symbolic",
        )

        self._power = Gtk.Button(
            icon_name="system-shutdown-symbolic",
        )

        self._home.set_hexpand(True)
        self._settings.set_hexpand(True)
        self._power.set_hexpand(True)

        self._home.connect(
            "clicked",
            self._on_home_clicked,
        )

        self._settings.connect(
            "clicked",
            self._on_settings_clicked,
        )

        self._power.connect(
            "clicked",
            self._on_power_clicked,
        )

        self.append(
            self._home,
        )

        self.append(
            self._settings,
        )

        self.append(
            self._power,
        )

    def _on_home_clicked(
        self,
        _: Gtk.Button,
    ) -> None:
        """Show the home page."""

        self._navigation_service.show(
            Page.HOME,
        )

    def _on_settings_clicked(
        self,
        _: Gtk.Button,
    ) -> None:
        """Show the settings page."""

        self._navigation_service.show(
            Page.SETTINGS,
        )

    def _on_power_clicked(
        self,
        _: Gtk.Button,
    ) -> None:
        """Show the power page."""

        self._navigation_service.show(
            Page.POWER,
        )