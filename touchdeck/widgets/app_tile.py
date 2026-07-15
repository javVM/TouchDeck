from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GObject, Gtk

from touchdeck.models.app_entry import AppEntry


class AppTile(Gtk.Button):
    """A touch-friendly tile representing a launchable application."""

    __gsignals__ = {
        "activated": (
            GObject.SignalFlags.RUN_FIRST,
            None,
            (object,),
        ),
    }

    def __init__(self, app: AppEntry) -> None:
        super().__init__()

        self._app = app

        self.set_size_request(140, 140)

        self._build_ui()
        self._connect_signals()

    def _build_ui(self) -> None:
        """Build the widget hierarchy."""

        self._box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12,
            halign=Gtk.Align.CENTER,
            valign=Gtk.Align.CENTER,
        )

        self._image = Gtk.Image(
            icon_name=self._app.icon,
            pixel_size=48,
        )

        self._label = Gtk.Label(
            label=self._app.title,
        )

        self._box.append(self._image)
        self._box.append(self._label)

        self.set_child(self._box)

    def _connect_signals(self) -> None:
        """Connect GTK signals."""

        self.connect("clicked", self._on_clicked)

    def _on_clicked(self, _: Gtk.Button) -> None:
        """Emit the activation signal."""

        self.emit(
            "activated",
            self._app,
        )