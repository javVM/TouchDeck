from __future__ import annotations

from dataclasses import dataclass

from touchdeck.enums.theme import Theme


@dataclass(slots=True)
class Settings:
    """Application settings."""

    theme: Theme = Theme.DARK

    grid_columns: int = 2

    clock_24h: bool = True

    def to_dict(self) -> dict[str, object]:
        """Serialize settings."""

        return {
            "theme": self.theme.value,
            "grid_columns": self.grid_columns,
            "clock_24h": self.clock_24h,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object],
    ) -> "Settings":
        """Create settings from dictionary."""

        return cls(
            theme=Theme(
                str(
                    data.get(
                        "theme",
                        Theme.DARK.value,
                    )
                )
            ),
            grid_columns=int(
                data.get(
                    "grid_columns",
                    2,
                )
            ),
            clock_24h=bool(
                data.get(
                    "clock_24h",
                    True,
                )
            ),
        )