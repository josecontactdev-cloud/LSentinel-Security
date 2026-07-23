import discord


class EmbedBuilder:
    """Utility class for creating consistent Discord embeds."""

    @staticmethod
    def success(title: str, description: str = "") -> discord.Embed:
        embed = discord.Embed(
            title=f"✅ {title}",
            description=description,
            color=discord.Color.green()
        )
        return embed

    @staticmethod
    def error(title: str, description: str = "") -> discord.Embed:
        embed = discord.Embed(
            title=f"❌ {title}",
            description=description,
            color=discord.Color.red()
        )
        return embed

    @staticmethod
    def info(title: str, description: str = "") -> discord.Embed:
        embed = discord.Embed(
            title=f"ℹ️ {title}",
            description=description,
            color=discord.Color.blue()
        )
        return embed

    @staticmethod
    def warning(title: str, description: str = "") -> discord.Embed:
        embed = discord.Embed(
            title=f"⚠️ {title}",
            description=description,
            color=discord.Color.orange()
        )
        return embed