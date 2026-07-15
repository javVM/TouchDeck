# Contributing to TouchDeck

First of all, thank you for your interest in contributing to TouchDeck.

TouchDeck aims to become a modern, touch-first shell for Raspberry Pi and Linux. The project values simplicity, maintainability and clean architecture above rapid feature development.

## Project Philosophy

Before writing code, please keep these principles in mind:

* Touch-first, not desktop-first.
* Simplicity over cleverness.
* Composition over complexity.
* Readability over brevity.
* Modularity over monolithic code.

Every component should have a single responsibility.

---

# Development Workflow

1. Create a feature branch.
2. Keep commits small and focused.
3. Ensure the project runs before opening a pull request.
4. Update documentation when introducing architectural changes.
5. Prefer incremental improvements over large rewrites.

---

# Coding Standards

## Python

* Follow modern Python practices.
* Use type annotations consistently.
* Prefer `pathlib` over `os.path`.
* Prefer `dataclasses` for models.
* Use `slots=True` for all data models.
* Avoid global variables.
* Keep functions small and focused.

---

## Architecture

TouchDeck follows a layered architecture:

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

Code should only depend on lower layers.

For example:

* Widgets may use models.
* Widgets may call services through injected dependencies.
* Services should never depend on widgets.

---

## Single Responsibility

Each class should have one clear purpose.

Good examples:

* `MainWindow`
* `HomePage`
* `AppTile`
* `LauncherService`
* `PowerService`

Avoid classes that perform unrelated tasks.

---

## UI

The user interface should remain independent from system logic.

Widgets should emit events.

Services should perform actions.

Avoid calling operating system commands directly from widgets.

---

## Styling

Keep visual styling inside CSS.

Avoid embedding styling logic into Python whenever possible.

---

## Imports

Use absolute imports.

Preferred:

```python
from touchdeck.models.app_entry import AppEntry
```

Avoid relative imports.

---

## Documentation

Public classes and methods should include clear docstrings when their purpose is not immediately obvious.

Architectural decisions should be documented.

---

# Code Formatting

The project uses:

* Ruff
* MyPy
* Pytest
* Pre-commit

Please ensure all checks pass before submitting changes.

---

# Pull Requests

A good pull request should:

* Solve a single problem.
* Include a clear description.
* Avoid unrelated refactoring.
* Update documentation if needed.

Small pull requests are preferred over large ones.

---

# Design Principles

When adding new features, ask yourself:

* Is this touch-friendly?
* Does it belong in this layer?
* Can this component be reused?
* Will this still make sense in a year?

If the answer is "no", consider a different design.

---

# Long-Term Vision

TouchDeck is intended to become a modular touch-first shell capable of hosting:

* Application launcher
* Media center
* Home automation dashboards
* Widgets
* Notifications
* System settings
* Plugin ecosystem

Every contribution should move the project toward that vision.

Thank you for helping build TouchDeck.
