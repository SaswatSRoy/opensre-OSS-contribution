"""CI vs local behavior for turn tests that may skip when prerequisites are missing."""

from __future__ import annotations

import os

import pytest


def skip_or_fail(message: str) -> None:
    """Fail in CI (required gate); skip locally (optional prerequisites)."""
    if os.getenv("GITHUB_ACTIONS", "").strip().lower() == "true":
        pytest.fail(message)
    pytest.skip(message)
