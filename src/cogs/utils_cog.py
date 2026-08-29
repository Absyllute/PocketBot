import discord
from discord.ext import commands
from discord import app_commands
from utils.embeds import BotEmbeds

class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='ping', description='A ping command to test if the bot is online')
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = BotEmbeds.ping_embed(latency)
        await  interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot=bot))