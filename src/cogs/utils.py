import discord
from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="uuid", description="Generate a random UUID.")
    async def uuid(self, interaction: discord.Interaction):
        import uuid

        generated = uuid.uuid4()

        await interaction.response.send_message(
            f"##ID **Generated UUID**\n\n`{generated}`"
        )

    @discord.app_commands.command(
        name="base64encode", description="Encode text into Base64."
    )
    @discord.app_commands.describe(text="Text to encode")
    async def base64encode(self, interaction: discord.Interaction, text: str):
        import base64

        encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")

        await interaction.response.send_message(
            f"🔒 **Base64 Encoded**\n\n" f"Input:\n`{text}`\n\n" f"Output:\n`{encoded}`"
        )

    @discord.app_commands.command(
        name="base64decode", description="Decode Base64 text."
    )
    @discord.app_commands.describe(encoded="Base64 text to decode")
    async def base64decode(self, interaction: discord.Interaction, encoded: str):
        import base64

        try:
            decoded = base64.b64decode(encoded).decode("utf-8")

            await interaction.response.send_message(
                f"🔓 **Base64 Decoded**\n\n"
                f"Input:\n`{encoded}`\n\n"
                f"Output:\n`{decoded}`"
            )

        except Exception:
            await interaction.response.send_message("❌ Invalid Base64 input.")

    @discord.app_commands.command(
        name="timestamp", description="Generate a Unix timestamp."
    )
    async def timestamp(self, interaction: discord.Interaction):
        import time

        unix_time = int(time.time())

        await interaction.response.send_message(
            f"⏱️ **Unix Timestamp**\n\n`{unix_time}`"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot))
