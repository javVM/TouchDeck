# TouchDeck

> A modern touch-first shell for Raspberry Pi and Linux.

TouchDeck is an open-source project that transforms Raspberry Pi and Linux devices into a modern touch interface designed specifically for touchscreens.

Instead of adapting a traditional desktop environment, TouchDeck provides a lightweight, modular and extensible shell capable of launching applications, displaying dashboards and integrating with external services such as Home Assistant.

---

# Vision

Traditional desktop environments were designed around a mouse and keyboard.

TouchDeck starts from a different premise:

> **Design for fingers, not cursors.**

The goal is to create a responsive, beautiful and modular interface that feels natural on touch devices while remaining lightweight enough to run on Raspberry Pi hardware.

---

# Goals

* Touch-first interface
* Modern GTK4 UI
* Wayland native
* Lightweight
* Modular architecture
* Easy to extend
* Raspberry Pi first
* Open source

---

# Planned Features

* Application launcher
* Home Assistant integration
* Kodi integration
* Media dashboard
* Camera dashboard
* Widgets
* Notifications
* Weather
* Calendar
* System settings
* Brightness control
* Volume control
* Power management
* Plugin system

---

# Technology Stack

| Component      | Technology     |
| -------------- | -------------- |
| Language       | Python 3       |
| GUI            | GTK4           |
| Design         | Libadwaita     |
| Display Server | Wayland        |
| Compositor     | Labwc          |
| Configuration  | JSON           |
| Styling        | CSS            |
| Packaging      | pyproject.toml |

---

# Architecture

TouchDeck follows a layered architecture.

```text
TouchDeckApplication
        │
        ▼
    MainWindow
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

Widgets never execute system commands directly.

Services encapsulate interactions with the operating system.

---

# Project Structure

```text
touchdeck/
│
├── core/
│   ├── application.py
│   ├── window.py
│   ├── navigation.py
│   └── config.py
│
├── models/
│
├── pages/
│
├── widgets/
│
├── services/
│
├── utils/
│
└── theme.css
```

---

# Development Principles

TouchDeck is built around a few simple principles.

## Touch First

Everything should be designed for touch interaction.

Large buttons.

Comfortable spacing.

Minimal navigation.

---

## Single Responsibility

Every class should have one responsibility.

Examples:

* MainWindow
* HomePage
* AppTile
* LauncherService
* PowerService

Avoid classes that do multiple unrelated things.

---

## Separation of Concerns

The UI should never know how the operating system works.

Example:

```text
AppTile

↓

activated signal

↓

HomePage

↓

LauncherService

↓

subprocess.Popen(...)
```

Widgets emit signals.

Services perform actions.

---

## Layered Dependencies

Dependencies always point downward.

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
    ↓
Models
```

Services never depend on widgets.

Models never depend on GTK.

---

# Coding Standards

## Modern Python

TouchDeck embraces modern Python.

Preferred features include:

* dataclasses
* slots=True
* pathlib
* enum
* typing
* match statements where appropriate

---

## Type Hints

Every public function should be typed.

Good:

```python
def launch(app: AppEntry) -> None:
    ...
```

Avoid:

```python
def launch(app):
    ...
```

---

## Data Models

Models should use dataclasses.

```python
@dataclass(slots=True)
class AppEntry:
    title: str
    icon: str
    command: str
```

Using `slots=True` improves memory usage and prevents accidental attribute creation.

---

## Private Members

Internal attributes should always use a leading underscore.

```python
self._window
self._launcher
self._apps
self._image
self._label
```

Avoid public attributes unless they are intentionally part of the class API.

---

## Methods

Private helper methods use a leading underscore.

```python
_build_ui()
_connect_signals()
_load_apps()
_update_clock()
_on_clicked()
```

Public methods expose the behavior of a component.

```python
launch()
navigate()
reload()
show_page()
```

---

## Constructors

Constructors should stay small.

Prefer this pattern:

```python
class AppTile(Gtk.Button):

    def __init__(self, app: AppEntry) -> None:
        super().__init__()

        self._app = app

        self._build_ui()
        self._connect_signals()
```

instead of placing all initialization logic directly inside `__init__()`.

---

## Styling

Business logic belongs in Python.

Visual appearance belongs in CSS.

Avoid embedding styling logic inside widgets.

---

## Imports

Use absolute imports.

Example:

```python
from touchdeck.models.app_entry import AppEntry
```

Avoid relative imports whenever possible.

---

## Documentation

Public classes should include concise docstrings.

Complex public methods should also be documented.

---

# Code Quality

The project uses modern tooling.

Planned tools include:

* Ruff
* MyPy
* Pytest
* pre-commit

---

# Scalability

TouchDeck is designed to evolve without major architectural changes.

Future features include:

* Plugin system
* Dynamic widgets
* Dashboard layouts
* User profiles
* Multiple pages
* Remote configuration
* Smart home integrations
* Package management

---

# Current Status

🚧 Early development

Current progress:

* GTK4 application
* Wayland support
* Main window
* Initial page system
* AppTile widget
* Launcher service
* Modular architecture

Next milestones:

* JSON application loader
* Home page grid
* CSS theme
* Icon support
* Settings page

---

# License

MIT License
