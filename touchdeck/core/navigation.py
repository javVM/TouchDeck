from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.core.services import Services
from touchdeck.enums.page import Page
from touchdeck.pages.home import HomePage
from touchdeck.pages.power import PowerPage
from touchdeck.pages.settings import SettingsPage


class NavigationStack(Gtk.Stack):
    """Application page navigation."""

    def __init__(
        self,
        services: Services,
    ) -> None:
        super().__init__()

        self._services = services

        self.set_hexpand(
            True,
        )

        self.set_vexpand(
            True,
        )

        self.set_transition_type(
            Gtk.StackTransitionType.SLIDE_LEFT_RIGHT,
        )

        self.set_transition_duration(
            250,
        )

        self.add_named(
            HomePage(
                config_service=self._services.config,
                launcher_service=self._services.launcher,
            ),
            Page.HOME.value,
        )

        self.add_named(
            SettingsPage(
                settings_service=self._services.settings,
            ),
            Page.SETTINGS.value,
        )

        self.add_named(
            PowerPage(),
            Page.POWER.value,
        )

        self.set_visible_child_name(
            Page.HOME.value,
        )

        self._services.navigation.attach_stack(
            self,
        )