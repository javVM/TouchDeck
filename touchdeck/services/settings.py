from __future__ import annotations

import json

from pathlib import Path

from touchdeck.models.settings import Settings


class SettingsService:
    """Manage application settings."""

    def __init__(self) -> None:

        self._config_path = (
            Path(__file__).resolve()
            .parent.parent.parent
            / "config"
            / "settings.json"
        )

        self._settings = self.load()

    @property
    def settings(self) -> Settings:
        """Current application settings."""

        return self._settings

    def load(self) -> Settings:
        """Load settings from disk."""

        if not self._config_path.exists():

            settings = Settings()

            self._settings = settings

            self.save()

            return settings

        try:

            with self._config_path.open(
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(file)

        except (
            json.JSONDecodeError,
            OSError,
        ):

            settings = Settings()

            self._settings = settings

            self.save()

            return settings

        settings = Settings.from_dict(
            data,
        )

        self._settings = settings

        return settings

    def save(self) -> None:
        """Save settings to disk."""

        self._config_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self._config_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                self._settings.to_dict(),
                file,
                indent=4,
            )