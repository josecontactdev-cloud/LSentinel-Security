"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Minimal project settings container."""

    bot_token: str = os.getenv("BOT_TOKEN", "")
    guild_id: int | None = None


settings = Settings()
