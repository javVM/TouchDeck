from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GObject, Gtk

from touchdeck.models.app_entry import AppEntry


class AppTile(Gtk.Button):
    """Touch-friendly application tile."""

    __gsignals__ = {
        "activated": (
            GObject.SignalFlags.RUN_FIRST,
            None,
            (object,),
        ),
    }

    def __init__(
        self,
        app: AppEntry,
    ) -> None:

        super().__init__()

        self._app = app

        self.set_size_request(
            140,
            140,
        )

        self.add_css_class(
            "app-tile"
        )

        self._build_ui()
        self._connect_signals()

    def _build_ui(self) -> None:
        """Build widget hierarchy."""

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12,
            halign=Gtk.Align.CENTER,
            valign=Gtk.Align.CENTER,
        )

        image = Gtk.Image(
            icon_name=self._app.icon,
            pixel_size=64,
        )

        image.add_css_class(
            "app-icon"
        )

        label = Gtk.Label(
            label=self._app.title,
        )

        label.add_css_class(
            "app-title"
        )

        box.append(image)
        box.append(label)

        self.set_child(box)

    def _connect_signals(self) -> None:
        """Connect widget signals."""

        self.connect(
            "clicked",
            self._on_clicked,
        )

    def _on_clicked(
        self,
        _: Gtk.Button,
    ) -> None:
        """Emit activation signal."""

        self.emit(
            "activated",
            self._app,
        )