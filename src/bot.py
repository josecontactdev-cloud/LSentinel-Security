import asyncio
from pathlib import Path

import discord
from discord.ext import commands

# Load the bot token from config.py (.env)
from config import DISCORD_TOKEN

# Enable only the default gateway intents.
# Additional intents will be enabled as new features are added.
intents = discord.Intents.default()

# Main bot instance.
# commands.Bot is the foundation that manages events, commands, and extensions.
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    # Register all slash commands with Discord.
    # This ensures any new commands become available.
    await bot.tree.sync()

    print(f"✅ Logged in as {bot.user}")


async def load_extensions():
    """
    Automatically load every Cog inside the cogs directory.
    Any new .py file will be loaded without modifying bot.py.
    """
    cogs_path = Path(__file__).parent / "cogs"

    for cog in cogs_path.glob("*.py"):
        if cog.name.startswith("__"):
            continue

        await bot.load_extension(f"cogs.{cog.stem}")
        print(f"✅ Loaded extension: {cog.stem}")


async def main():
    # Keep the bot alive inside a managed asynchronous context.
    async with bot:
        await load_extensions()

        # Connect to Discord using the token stored in .env.
        await bot.start(DISCORD_TOKEN)


# Application entry point.
# Starts the asynchronous event loop.
asyncio.run(main())