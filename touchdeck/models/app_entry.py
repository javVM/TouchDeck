from dataclasses import dataclass


@dataclass(slots=True)
class AppEntry:
    title: str
    icon: str
    command: str