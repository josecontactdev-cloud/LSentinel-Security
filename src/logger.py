"""Logging utilities for the project."""

from __future__ import annotations

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("lsentinel")
