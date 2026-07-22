import discord
import aiohttp
from discord.ext import commands


class Network(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="iplookup",
        description="Get public information about an IP address."
    )
    @discord.app_commands.describe(
        ip="IP address to lookup"
    )
    async def iplookup(
        self,
        interaction: discord.Interaction,
        ip: str
    ):
        await interaction.response.defer()

        try:
            url = f"https://ipwho.is/{ip}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()

            if not data.get("success"):
                await interaction.followup.send(
                    "❌ Invalid IP address."
                )
                return

            embed = discord.Embed(
                title="🌐 IP Information",
                color=discord.Color.blue()
            )

            embed.add_field(
                name="IP",
                value=data.get("ip", "Unknown"),
                inline=False
            )

            embed.add_field(
                name="Country",
                value=data.get("country", "Unknown"),
                inline=True
            )

            embed.add_field(
                name="City",
                value=data.get("city", "Unknown"),
                inline=True
            )

            embed.add_field(
                name="ISP",
                value=data.get("connection", {}).get("isp", "Unknown"),
                inline=False
            )

            embed.add_field(
                name="Organization",
                value=data.get("connection", {}).get("org", "Unknown"),
                inline=False
            )

            embed.add_field(
                name="ASN",
                value=data.get("connection", {}).get("asn", "Unknown"),
                inline=False
            )

            await interaction.followup.send(embed=embed)

        except Exception as e:
            await interaction.followup.send(
                f"❌ Error:\n`{e}`"
            )
            
async def setup(bot: commands.Bot):
    await bot.add_cog(Network(bot))
    
