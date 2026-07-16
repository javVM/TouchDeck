from __future__ import annotations

from touchdeck.models.settings import Settings


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