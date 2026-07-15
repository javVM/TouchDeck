from __future__ import annotations

import json
from pathlib import Path

from touchdeck.models.app_entry import AppEntry


class ConfigService:
    """Loads application configuration from disk."""

    def __init__(self) -> None:
        self._assets_path = (
            Path(__file__).resolve().parent.parent.parent / "assets"
        )

    def load_apps(self) -> list[AppEntry]:
        """Load launcher applications."""

        apps_file = self._assets_path / "apps.json"

        with apps_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return [
            AppEntry.from_dict(item)
            for item in data
        ]