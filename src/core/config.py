import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""

    DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")

    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    DEFAULT_EMBED_COLOR: int = 0x3498DB

    BOT_NAME: str = "LSentinel"

    VERSION: str = "0.1.0"

    @classmethod
    def validate(cls) -> None:
        if not cls.DISCORD_TOKEN:
            raise ValueError("DISCORD_TOKEN was not found in the .env file.")
