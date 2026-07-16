from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from touchdeck.enums.page import Page


class NavigationService:
    """Application navigation service."""

    def __init__(self) -> None:
        self._stack: Gtk.Stack | None = None

    def attach_stack(
        self,
        stack: Gtk.Stack,
    ) -> None:
        """Attach a navigation stack."""

        self._stack = stack

    def show(
        self,
        page: Page,
    ) -> None:
        """Show a page."""

        if self._stack is None:
            raise RuntimeError(
                "Navigation stack is not bound."
            )

        self._stack.set_visible_child_name(
            page.value,
        )

    def current_page(
        self,
    ) -> Page:
        """Return the current page."""

        if self._stack is None:
            raise RuntimeError(
                "Navigation stack is not bound."
            )

        name = self._stack.get_visible_child_name()

        return Page(name)