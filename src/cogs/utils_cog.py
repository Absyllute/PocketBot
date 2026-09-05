import discord
from discord.ext import commands
from discord import app_commands
from utils.embeds import BotEmbeds
from modals.embed_builder_modal_ import EmbedBuilderModal
from mcstatus import JavaServer
import utils.shared_vars as SharedVars

class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    embed_cmd_grp = app_commands.Group(name="embed", description="Commands for to make and edit pretty embeds")

    @embed_cmd_grp.command(name="builder", description="Create an embed from scratch")
    async def builder(self, interaction: discord.Interaction):
        await interaction.response.send_modal(EmbedBuilderModal())

    @app_commands.command(name='ping', description='A ping command to test if the bot is online')
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = BotEmbeds.ping_embed(latency)
        await  interaction.response.send_message(embed=embed)

    @app_commands.command(name="help", description="Shows a list of commands that PocketBot comes with")
    async def help(self, interaction: discord.Interaction):
        embed = BotEmbeds.help_embed()

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='about', description='Information about the bot')
    async def about(self, interaction: discord.Interaction):
        embed, bot_icon, dev_icon = BotEmbeds.about_embed(ver="v0.1.0")
        await interaction.response.send_message(embed=embed, files=[bot_icon, dev_icon])

async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot=bot))