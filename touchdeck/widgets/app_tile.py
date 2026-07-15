import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.models.app_entry import AppEntry


class AppTile(Gtk.Button):
    def __init__(self, app: AppEntry):
        super().__init__()

        self.app = app

        self.set_size_request(140, 140)

        self.set_child(
            Gtk.Label(label=app.title)
        )