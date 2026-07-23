import discord
from discord.ext import commands

from services.network_service import NetworkService
from utils.validators import Validator


class Network(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="iplookup", description="Get public information about an IP address."
    )
    async def iplookup(self, interaction: discord.Interaction, ip: str):
        await interaction.response.defer()

        try:
            ip = Validator.validate_ip(ip)

            data = await NetworkService.ip_lookup(ip)

            if not data.get("success"):
                await interaction.followup.send("❌ Invalid IP address.")
                return

            embed = discord.Embed(title="🌐 IP Information", color=discord.Color.blue())

            embed.add_field(name="IP", value=data.get("ip", "Unknown"), inline=False)

            embed.add_field(name="Country", value=data.get("country", "Unknown"))

            embed.add_field(name="City", value=data.get("city", "Unknown"))

            embed.add_field(
                name="ISP", value=data["connection"].get("isp", "Unknown"), inline=False
            )

            await interaction.followup.send(embed=embed)

        except Exception as error:
            await interaction.followup.send(f"❌ Error: `{error}`")

    @discord.app_commands.command(
        name="dnslookup", description="Lookup DNS records of a domain."
    )
    async def dnslookup(self, interaction: discord.Interaction, domain: str):
        await interaction.response.defer()

        try:
            domain = Validator.validate_domain(domain)

            records = NetworkService.dns_lookup(domain)

            embed = discord.Embed(
                title=f"🌐 DNS Lookup: {domain}", color=discord.Color.blue()
            )

            for name, values in records.items():

                embed.add_field(
                    name=name,
                    value="\n".join(values) if values else "No records found",
                    inline=False,
                )

            await interaction.followup.send(embed=embed)

        except Exception as error:
            await interaction.followup.send(f"❌ Error: `{error}`")


async def setup(bot: commands.Bot):
    await bot.add_cog(Network(bot))
