import discord
import whois
from discord import app_commands
from discord.ext import commands


class Osint(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="whois", description="Retrieve WHOIS information for a domain."
    )
    @app_commands.describe(domain="Domain name (example.com)")
    async def whois_lookup(self, interaction: discord.Interaction, domain: str):
        await interaction.response.defer()

        try:
            result = whois.whois(domain)

            embed = discord.Embed(
                title="🌐 WHOIS Lookup", color=discord.Color.dark_blue()
            )

            embed.add_field(
                name="Domain", value=result.domain_name or "Unknown", inline=False
            )

            embed.add_field(
                name="Registrar", value=result.registrar or "Unknown", inline=False
            )

            embed.add_field(
                name="Creation Date", value=str(result.creation_date), inline=False
            )

            embed.add_field(
                name="Expiration Date", value=str(result.expiration_date), inline=False
            )

            embed.add_field(
                name="Name Servers",
                value=(
                    "\n".join(result.name_servers[:5])
                    if result.name_servers
                    else "Unknown"
                ),
                inline=False,
            )

            embed.add_field(name="Status", value=str(result.status), inline=False)

            await interaction.followup.send(embed=embed)

        except Exception as error:
            await interaction.followup.send(f"❌ WHOIS lookup failed.\n```{error}```")


async def setup(bot: commands.Bot):
    await bot.add_cog(Osint(bot))
