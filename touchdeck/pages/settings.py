from __future__ import annotations

import gi

gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk

from touchdeck.services.settings import SettingsService
from touchdeck.models.theme import Theme


class SettingsPage(Adw.PreferencesPage):
    """Application settings page."""

    def __init__(
        self,
        settings_service: SettingsService,
    ) -> None:
        super().__init__()

        self._settings_service = settings_service

        self.set_title(
            "Settings",
        )

        self._build_ui()

    def _build_ui(self) -> None:
        """Build page."""

        self.add(
            self._build_appearance_group(),
        )

        self.add(
            self._build_launcher_group(),
        )

        self.add(
            self._build_clock_group(),
        )

        self._connect_signals()

    def _build_appearance_group(
        self,
    ) -> Adw.PreferencesGroup:
        """Build appearance settings."""

        group = Adw.PreferencesGroup(
            title="Appearance",
        )

        self._theme_switch = Gtk.Switch(
            active=(
                self._settings_service.settings.theme.value
                == "dark"
            ),
        )

        row = Adw.ActionRow(
            title="Dark theme",
        )

        row.add_suffix(
            self._theme_switch,
        )

        row.set_activatable_widget(
            self._theme_switch,
        )

        group.add(
            row,
        )

        return group

    def _build_launcher_group(
        self,
    ) -> Adw.PreferencesGroup:
        """Build launcher settings."""

        group = Adw.PreferencesGroup(
            title="Launcher",
        )

        adjustment = Gtk.Adjustment(
            value=self._settings_service.settings.grid_columns,
            lower=2,
            upper=6,
            step_increment=1,
        )

        self._columns = Gtk.SpinButton(
            adjustment=adjustment,
        )

        row = Adw.ActionRow(
            title="Grid columns",
        )

        row.add_suffix(
            self._columns,
        )

        row.set_activatable_widget(
            self._columns,
        )

        group.add(
            row,
        )

        return group

    def _build_clock_group(
        self,
    ) -> Adw.PreferencesGroup:
        """Build clock settings."""

        group = Adw.PreferencesGroup(
            title="Clock",
        )

        self._clock = Gtk.Switch(
            active=self._settings_service.settings.clock_24h,
        )

        row = Adw.ActionRow(
            title="24-hour format",
        )

        row.add_suffix(
            self._clock,
        )

        row.set_activatable_widget(
            self._clock,
        )

        group.add(
            row,
        )

        return group
    
    def _connect_signals(self) -> None:
        """Connect widget signals."""

        self._theme_switch.connect(
            "notify::active",
            self._on_theme_changed,
        )

        self._columns.connect(
            "value-changed",
            self._on_columns_changed,
        )

        self._clock.connect(
            "notify::active",
            self._on_clock_changed,
        )

    def _on_theme_changed(
        self,
        switch: Gtk.Switch,
        _: object,
    ) -> None:
        """Update theme setting."""

        theme = (
            Theme.DARK
            if switch.get_active()
            else Theme.LIGHT
        )

        self._settings_service.set_theme(
            theme,
        )


    def _on_columns_changed(
        self,
        spin: Gtk.SpinButton,
    ) -> None:
        """Update launcher columns."""

        self._settings_service.set_grid_columns(
            spin.get_value_as_int(),
        )


    def _on_clock_changed(
        self,
        switch: Gtk.Switch,
        _: object,
    ) -> None:
        """Update clock format."""

        self._settings_service.set_clock_24h(
            switch.get_active(),
        )