import asyncio
from pathlib import Path

import discord
from discord.ext import commands

from core.config import Config
from core.logger import get_logger

logger = get_logger(__name__)

# Enable only the default gateway intents.
intents = discord.Intents.default()

# Main bot instance.
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """Executed when the bot successfully connects to Discord."""
    await bot.tree.sync()
    logger.info(f"Logged in as {bot.user}")


async def load_extensions() -> None:
    """Automatically load every Cog inside the cogs directory."""

    cogs_path = Path(__file__).parent / "cogs"

    for cog in cogs_path.glob("*.py"):
        if cog.name.startswith("__"):
            continue

        await bot.load_extension(f"cogs.{cog.stem}")
        logger.info(f"Loaded extension: {cog.stem}")


async def main() -> None:
    """Application entry point."""

    Config.validate()

    async with bot:
        await load_extensions()
        await bot.start(Config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
