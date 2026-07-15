import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.models.app_entry import AppEntry
from touchdeck.widgets.app_tile import AppTile


class HomePage(Gtk.Box):

    def __init__(self):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=20,
        )

        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)

        grid = Gtk.Grid(
            row_spacing=20,
            column_spacing=20,
        )

        apps = [
            AppEntry("Chromium", "web-browser", "chromium"),
            AppEntry("Kodi", "kodi", "kodi"),
            AppEntry("Terminal", "terminal", "foot"),
            AppEntry("Files", "files", "pcmanfm"),
        ]

        row = 0
        col = 0

        for app in apps:

            tile = AppTile(app)

            grid.attach(tile, col, row, 1, 1)

            col += 1

            if col == 2:
                col = 0
                row += 1

        self.append(grid)