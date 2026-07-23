import socket
import ssl
from datetime import datetime

import discord
from discord.ext import commands


class Security(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="sslcheck", description="Check SSL certificate information of a domain."
    )
    @discord.app_commands.describe(domain="Domain to check (example.com)")
    async def sslcheck(self, interaction: discord.Interaction, domain: str):
        try:
            context = ssl.create_default_context()

            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:

                    cert = ssock.getpeercert()

            issuer = dict(x[0] for x in cert["issuer"])
            subject = dict(x[0] for x in cert["subject"])

            expires = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")

            embed = discord.Embed(
                title="🔒 SSL Certificate Check", color=discord.Color.green()
            )

            embed.add_field(name="Domain", value=domain, inline=False)

            embed.add_field(
                name="Issuer",
                value=issuer.get("organizationName", "Unknown"),
                inline=False,
            )

            embed.add_field(
                name="Subject", value=subject.get("commonName", "Unknown"), inline=False
            )

            embed.add_field(
                name="Expires", value=expires.strftime("%Y-%m-%d"), inline=False
            )

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(f"❌ SSL check failed:\n`{e}`")


async def setup(bot: commands.Bot):
    await bot.add_cog(Security(bot))
