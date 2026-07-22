import discord
from discord import app_commands
from discord.ext import commands

from config import DISCORD_TOKEN

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Logged in as {bot.user}")


@bot.tree.command(name="ping", description="Check the bot latency.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! `{round(bot.latency * 1000)} ms`"
    )


bot.run(DISCORD_TOKEN)