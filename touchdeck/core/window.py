import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from touchdeck.pages.home import HomePage


class MainWindow(Adw.ApplicationWindow):

    def __init__(self, application):

        super().__init__(application=application)

        self.set_title("TouchDeck")

        self.fullscreen()

        self.set_content(HomePage())