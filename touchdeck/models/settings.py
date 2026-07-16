from __future__ import annotations

from dataclasses import dataclass

from touchdeck.enums.theme import Theme


@dataclass(slots=True)
class Settings:
    """Application settings."""

    theme: Theme = Theme.DARK

    grid_columns: int = 2

    clock_24h: bool = True