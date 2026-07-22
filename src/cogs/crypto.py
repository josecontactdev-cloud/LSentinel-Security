import discord
from discord.ext import commands


class Crypto(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="hash",
        description="Generate a SHA-256 hash from text."
    )
    async def hash(self, interaction: discord.Interaction, text: str):
        import hashlib

        hashed = hashlib.sha256(text.encode()).hexdigest()

        await interaction.response.send_message(
            f"🔐 **SHA-256 Hash**\n\n"
            f"**Input:**\n{text}\n\n"
            f"**Hash:**\n`{hashed}`"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Crypto(bot))