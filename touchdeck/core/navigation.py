from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.pages.home import HomePage


class NavigationStack(Gtk.Stack):
    """Application page navigation."""

    def __init__(self) -> None:

        super().__init__()

        self.set_transition_type(
            Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )

        self.set_transition_duration(
            250
        )

        self.add_named(
            HomePage(),
            "home",
        )

        self.set_visible_child_name(
            "home"
        )

    def show(
        self,
        page: str,
    ) -> None:
        """Show a registered page."""

        self.set_visible_child_name(
            page
        )