import discord
from discord import app_commands
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- --- --- Purge Any --- --- --- #
    @app_commands.command(name="purge-any", description="Mass delete a configurable amount of messages")
    async def purge(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            deleted = await interaction.channel.purge(limit=amount)

            await interaction.followup.send(f"Deleted {len(deleted)} messages!")
        else:
            await interaction.followup.send("Unable to purge messages in this channel", ephemeral=True)

    # --- --- --- Purge Human --- --- --- #
    @app_commands.command(name="purge-human", description="Mass delete a configurable amount of messages made by humans (non-nots)")
    async def human_purge(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            def is_human(msg: discord.Message) -> bool:
                return not msg.author.bot

            messages_deleted = await interaction.channel.purge(limit=amount, check=is_human)

            await interaction.followup.send(f"Deleted {len(messages_deleted)} human messages! (bots skipped)", ephemeral=True)
        else:
            await interaction.followup.send("Unable to purge messages in this channel")

async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot=bot))