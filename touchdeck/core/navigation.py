from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.enums.page import Page
from touchdeck.pages.home import HomePage
from touchdeck.pages.power import PowerPage
from touchdeck.pages.settings import SettingsPage
from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.services.navigation import NavigationService
from touchdeck.services.settings import SettingsService


class NavigationStack(Gtk.Stack):
    """Application page navigation."""

    def __init__(
        self,
        config_service: ConfigService,
        launcher_service: LauncherService,
        navigation_service: NavigationService,
        settings_service: SettingsService,
    ) -> None:
        super().__init__()

        self.set_hexpand(True)
        self.set_vexpand(True)

        self.set_transition_type(
            Gtk.StackTransitionType.SLIDE_LEFT_RIGHT,
        )

        self.set_transition_duration(
            250,
        )

        self.add_named(
            HomePage(
                config_service=config_service,
                launcher_service=launcher_service,
            ),
            Page.HOME.value,
        )

        self.add_named(
            SettingsPage(
                settings_service=settings_service,
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

        navigation_service.attach_stack(
            self,
        )