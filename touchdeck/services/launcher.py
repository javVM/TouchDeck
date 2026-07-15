from __future__ import annotations

import subprocess

from touchdeck.models.app_entry import AppEntry


class LauncherService:
    """Launch desktop applications."""

    def launch(self, app: AppEntry) -> None:
        subprocess.Popen(
            app.command,
            start_new_session=True,
        )