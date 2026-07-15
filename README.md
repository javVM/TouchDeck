# TouchDeck

**A modular touch-first shell for Raspberry Pi and Linux, built with GTK4 and Wayland.**

TouchDeck is an open-source project that aims to transform Raspberry Pi and other Linux devices into modern touch-first systems.

Instead of adapting a traditional desktop environment, TouchDeck provides a clean, intuitive interface designed specifically for touchscreens. Whether you're building a home automation panel, a media center, a wall-mounted dashboard, or a dedicated kiosk, TouchDeck provides a lightweight and extensible foundation.

---

# Vision

Traditional Linux desktop environments are designed around a mouse and keyboard.

TouchDeck starts from a different premise:

> **Build a desktop designed for fingers, not cursors.**

The project focuses on simplicity, responsiveness and modularity while taking advantage of modern Linux technologies such as Wayland and GTK4.

TouchDeck is not just an application launcher.

It is intended to become a complete touch-first shell capable of hosting media applications, smart home dashboards, system controls and future plugins.

---

# Goals

* Build a modern touch-first desktop experience.
* Replace traditional desktop paradigms with a simplified UI.
* Keep the project lightweight and responsive.
* Maintain a clean and scalable architecture.
* Be fully configurable.
* Support Raspberry Pi as a first-class platform.
* Remain modular and extensible.
* Follow modern Python development practices.

---

# Planned Features

* Touch-first launcher
* Fullscreen shell
* Home Assistant integration
* Kodi integration
* Media dashboard
* System settings
* Notifications
* Weather widgets
* Calendar
* Camera monitoring
* Network management
* Brightness & volume controls
* Power management
* Plugin system

---

# Technology Stack

| Component      | Technology     |
| -------------- | -------------- |
| Language       | Python 3       |
| UI Toolkit     | GTK4           |
| Design Library | Libadwaita     |
| Display Server | Wayland        |
| Compositor     | Labwc          |
| Styling        | CSS            |
| Configuration  | JSON           |
| Packaging      | pyproject.toml |

---

# High-Level Architecture

```text
TouchDeckApplication
        │
        ▼
    MainWindow
        │
        ▼
    Navigation
        │
        ▼
       Pages
        │
        ▼
      Widgets
        │
        ▼
      Services
        │
        ▼
       Models
```

Each layer has a single responsibility.

The UI should never communicate directly with the operating system.

Instead, widgets emit events and services execute the corresponding system actions.

---

# Project Structure

```text
touchdeck/
│
├── touchdeck/
│   │
│   ├── core/
│   │   ├── application.py
│   │   ├── window.py
│   │   ├── navigation.py
│   │   └── config.py
│   │
│   ├── models/
│   │
│   ├── pages/
│   │
│   ├── widgets/
│   │
│   ├── services/
│   │
│   ├── utils/
│   │
│   └── theme.css
│
├── assets/
│
├── pyproject.toml
│
└── README.md
```

---

# Design Principles

## Touch First

Every interface element should be designed for touch interaction.

Large buttons, generous spacing and simple navigation are preferred over traditional desktop layouts.

---

## Modularity

Every feature should be implemented as an independent component.

Future modules should be added without modifying the application's core.

Examples include:

* Home Assistant
* Jellyfin
* Spotify
* Frigate
* MQTT
* Camera dashboards
* Custom plugins

---

## Separation of Concerns

Each class should have a single responsibility.

For example:

* `MainWindow` hosts pages.
* `HomePage` displays applications.
* `AppTile` renders a single application.
* `LauncherService` launches applications.
* `PowerService` handles shutdown and reboot.

Widgets never execute system commands directly.

---

## Layered Architecture

```text
UI
 │
 ▼
Pages
 │
 ▼
Widgets
 │
 ▼
Services
 │
 ▼
Models
```

This separation keeps the application maintainable as it grows.

---

# Development Guidelines

## Modern Python

TouchDeck follows modern Python practices.

Preferred language features include:

* dataclasses
* slots
* pathlib
* enum
* typing
* match statements where appropriate

---

## Strong Typing

All public code should use type annotations.

Example:

```python
def launch(app: AppEntry) -> None:
    ...
```

Untyped functions should be avoided.

---

## Data Models

Application data is represented using dataclasses.

Example:

```python
@dataclass(slots=True)
class AppEntry:
    title: str
    icon: str
    command: str
```

Using `slots=True` improves memory efficiency and prevents accidental attribute creation.

---

## Dependency Direction

Dependencies should always point downward.

```text
Application
    ↓
Window
    ↓
Pages
    ↓
Widgets
    ↓
Services
```

Widgets should never instantiate services internally.

Dependencies should be injected whenever possible.

---

## Styling

Visual appearance belongs in CSS.

Business logic belongs in Python.

Avoid embedding styling directly inside widgets.

---

## Imports

Use absolute imports throughout the project.

Example:

```python
from touchdeck.models.app_entry import AppEntry
```

Avoid relative imports unless there is a compelling reason.

---

# Scalability

TouchDeck is designed to evolve into a complete touch-first shell.

The architecture should support future features such as:

* Multiple pages
* Plugin system
* Dynamic widgets
* Dashboard layouts
* Application categories
* Favorites
* User profiles
* Remote configuration
* Package management
* Smart home integrations

without requiring changes to the application's core.

---

# Code Quality

The project aims to maintain high code quality from the beginning.

Planned tooling includes:

* Ruff
* MyPy
* Pytest
* Pre-commit hooks

Quality and maintainability are considered first-class features.

---

# Current Status

🚧 Early development

Current milestone:

* Basic GTK4 application
* Fullscreen window
* Initial architecture
* Page system
* Data model

Next milestone:

* Material-style application tiles
* Launcher service
* Navigation system
* Theme engine

---

# License

MIT License
