from __future__ import annotations

from touchdeck.models.settings import Settings
from touchdeck.enums.theme import Theme


class SettingsService:
    """Manage application settings."""

    def __init__(self) -> None:
        self._settings = self.load()

    @property
    def settings(self) -> Settings:
        """Return current settings."""

        return self._settings

    def load(self) -> Settings:
        """Load settings."""

        return Settings()

    def save(self) -> None:
        """Persist settings."""

        raise NotImplementedError

    def set_theme(
        self,
        theme: Theme,
    ) -> None:
        self._settings.theme = theme

    def set_grid_columns(
        self,
        columns: int,
    ) -> None:
        self._settings.grid_columns = columns

    def set_clock_24h(
        self,
        enabled: bool,
    ) -> None:
        self._settings.clock_24h = enabled