# TouchDeck

**A modular touch-first desktop for Raspberry Pi and Linux, built with GTK4 and Wayland.**

TouchDeck is an open-source project that aims to transform Raspberry Pi and other Linux devices into modern touch-first systems.

Rather than adapting a traditional desktop environment, TouchDeck provides a clean, intuitive interface designed specifically for touchscreens. Whether you're building a home automation panel, a media center, a wall-mounted dashboard or a dedicated kiosk, TouchDeck provides a lightweight and extensible foundation.

---

## Vision

Traditional Linux desktop environments are designed around a mouse and keyboard.

TouchDeck starts from a different premise:

> Build a desktop designed for fingers, not cursors.

The project focuses on simplicity, responsiveness and modularity while taking advantage of modern Linux technologies such as Wayland and GTK4.

---

## Features

- Touch-first interface
- Fullscreen launcher
- Modular architecture
- Wayland native
- GTK4 + Libadwaita UI
- Lightweight
- Configurable
- Extensible
- Open source

---

## Planned Modules

- Application Launcher
- Media Center (Kodi)
- Home Assistant integration
- System Settings
- Notifications
- Widgets
- Weather
- Calendar
- Cameras
- Network Management
- Brightness & Volume controls
- Power Management

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3 |
| UI Toolkit | GTK4 |
| Design Library | Libadwaita |
| Display Server | Wayland |
| Compositor | Labwc |
| Styling | CSS |
| Configuration | JSON |
| Packaging | pyproject.toml |

---

## Project Architecture

```
TouchDeck
│
├── Core
│   ├── Application
│   ├── Window Manager
│   ├── Configuration
│   └── Navigation
│
├── UI
│   ├── Pages
│   ├── Widgets
│   ├── Components
│   └── Themes
│
├── Services
│   ├── App Launcher
│   ├── Notifications
│   ├── System APIs
│   └── Power Management
│
└── Modules
    ├── Home
    ├── Media
    ├── Dashboard
    ├── Settings
    └── Future Extensions
```

---

## Scalability

TouchDeck is designed around modular components.

Each feature should be self-contained and reusable, allowing new functionality to be added without modifying the core application.

Future modules may include:

- Home Assistant
- Jellyfin
- Spotify
- Frigate
- MQTT
- Smart Home dashboards
- Camera monitoring
- Custom plugins

---

## Goals

- Create a modern touch interface for Linux.
- Provide a fast and lightweight experience.
- Avoid traditional desktop paradigms.
- Be fully configurable.
- Support Raspberry Pi as a first-class platform.
- Remain modular and easy to extend.

---

## Development Status

🚧 Early development

The project is currently in its initial architecture and design phase.

---

## License

MIT License
