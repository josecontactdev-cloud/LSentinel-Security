import discord
from discord.ext import commands


class Crypto(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="hash",
        description="Generate a hash from text using a selected algorithm."
    )
    @discord.app_commands.describe(
        text="Text to hash",
        algorithm="Hash algorithm (sha256, sha512, sha1, md5, blake2b)"
    )
    async def hash(
        self,
        interaction: discord.Interaction,
        text: str,
        algorithm: str = "sha256"
    ):
        import hashlib

        algorithms = {
            "sha256": hashlib.sha256,
            "sha512": hashlib.sha512,
            "sha1": hashlib.sha1,
            "md5": hashlib.md5,
            "blake2b": hashlib.blake2b
        }

        algorithm = algorithm.lower()

        if algorithm not in algorithms:
            await interaction.response.send_message(
                "❌ Invalid algorithm.\n"
                "Available: sha256, sha512, sha1, md5, blake2b"
            )
            return

        hashed = algorithms[algorithm](text.encode()).hexdigest()

        embed = discord.Embed(
            title="🔐 Hash Generated",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="Algorithm",
            value=algorithm.upper(),
            inline=False
        )

        embed.add_field(
            name="Input",
            value=f"`{text}`",
            inline=False
        )

        embed.add_field(
            name="Hash",
            value=f"`{hashed}`",
            inline=False
        )

        await interaction.response.send_message(embed=embed)
        
    @discord.app_commands.command(
        name="hashfile",
        description="Generate hashes from an uploaded file."
    )
    async def hashfile(
        self,
        interaction: discord.Interaction,
        file: discord.Attachment
    ):
        import hashlib

        data = await file.read()

        sha256 = hashlib.sha256(data).hexdigest()
        sha512 = hashlib.sha512(data).hexdigest()
        md5 = hashlib.md5(data).hexdigest()

        embed = discord.Embed(
            title="📁 File Hash Generated",
            color=discord.Color.green()
        )

        embed.add_field(
            name="File",
            value=file.filename,
            inline=False
        )

        embed.add_field(
            name="Size",
            value=f"{file.size} bytes",
            inline=False
        )

        embed.add_field(
            name="SHA-256",
            value=f"`{sha256}`",
            inline=False
        )

        embed.add_field(
            name="SHA-512",
            value=f"`{sha512}`",
            inline=False
        )

        embed.add_field(
            name="MD5",
            value=f"`{md5}`",
            inline=False
        )

        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Crypto(bot))
    