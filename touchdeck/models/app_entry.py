from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AppEntry:
    """Represents a launchable application."""

    title: str
    icon: str
    command: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "AppEntry":
        """Create an AppEntry from a dictionary."""

        return cls(
            title=data["title"],
            icon=data["icon"],
            command=data["command"],
        )