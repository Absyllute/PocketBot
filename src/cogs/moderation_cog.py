import discord
from discord import app_commands
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="purge", description="Mass delete a configurable amount of messages")
    async def purge(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            deleted = await interaction.channel.purge(limit=amount)

            await interaction.followup.send(f"Deleted {len(deleted)} messages!")
        else:
            await interaction.followup.send("Unable to purge messages in this channel", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot=bot))