# daemonless: the SQLite database and uploads live in /config. Everything
# else is upstream's environment-driven base settings.
import os

from .base import *  # noqa: F401,F403

if not os.getenv("DATABASE_URL") and not os.getenv("DB_NAME"):
    if DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3":  # noqa: F405
        DATABASES["default"]["NAME"] = "/config/db.sqlite3"  # noqa: F405

MEDIA_ROOT = "/config/media"
