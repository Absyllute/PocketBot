from discord import app_commands, Interaction
from discord.ext import commands
from utils.embeds import BotEmbeds
from mcstatus import JavaServer
import utils.shared_vars as SharedVars

class SMP(commands.Cog):
    def __int__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ip", description="View the join link for the PocketCraft SMP")
    async def ip(self, interaction: Interaction):

        await interaction.response.send_message(embed=BotEmbeds.ip_embed())

    @app_commands.command(name="smpstatus", description="View the status of the SMP")
    async def smpstatus(self, interaction: Interaction):
        await interaction.response.defer()

        try:
            server = await JavaServer.async_lookup(SharedVars.smp_link)
            status = await server.async_status()


            eb = BotEmbeds.smp_embed(latency=round(status.latency), online_players=status.players.online)
        except Exception as e:
            if "[Errno 104] Connection reset by peer" in str(e) or isinstance(e, ConnectionResetError):
                eb = BotEmbeds.smp_error_embed(str(e))
                print(f"Failed to send: \"{e}\"")

                eb.add_field(
                    name="Try running the command again...",
                    value=""
                )
            else:
                print(f"Failed to send: \"{e}\"")
                eb = BotEmbeds.smp_error_embed(str(e))

        await interaction.followup.send(embed=eb)


async def setup(bot: commands.Bot):
    await bot.add_cog(SMP(bot))
