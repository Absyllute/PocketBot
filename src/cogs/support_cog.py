import discord
from discord.ext import commands
from discord import app_commands
from modals.log_send_modal import LogSenderModal

class Support(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    log_cmd_grp = app_commands.Group(name="logs", description="Commands relating to minecraft server logs")

    @log_cmd_grp.command(name="send", description="Upload your logs, regardless of Discord's character")
    async def logs_send(self, interaction: discord.Interaction):
        await interaction.response.send_modal(LogSenderModal())

async def setup(bot: commands.Bot):
    await bot.add_cog(Support(bot=bot))
