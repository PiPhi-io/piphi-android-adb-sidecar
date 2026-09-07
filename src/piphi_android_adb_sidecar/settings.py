from __future__ import annotations

import os

INTEGRATION_ID = "piphi-android-adb-sidecar"
INTEGRATION_NAME = "Piphi Android Adb Sidecar"
INTEGRATION_VERSION = "0.1.0"
PROJECT_KIND = "sidecar"
PROJECT_PRESET = "sidecar-worker"
PROJECT_DOMAIN = "sidecar-service"
DEFAULT_PORT = 4213


def runtime_port() -> int:
    raw_port = os.getenv("PORT", str(DEFAULT_PORT))
    try:
        return int(raw_port)
    except ValueError:
        return DEFAULT_PORT
