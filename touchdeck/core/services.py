from __future__ import annotations

from touchdeck.services.config import ConfigService
from touchdeck.services.launcher import LauncherService
from touchdeck.services.navigation import NavigationService
from touchdeck.services.settings import SettingsService
from touchdeck.services.theme import ThemeService


class Services:
    """Application services."""

    def __init__(self) -> None:

        self.settings = SettingsService()

        self.navigation = NavigationService()

        self.config = ConfigService()

        self.launcher = LauncherService()

        self.theme = ThemeService(
            self.settings,
        )