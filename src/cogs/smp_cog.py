from discord import app_commands, Interaction
from discord.ext import commands
from utils.embeds import BotEmbeds
from modals.join_link_modal import JoinLinkModal
from mcstatus import JavaServer
import utils.shared_vars as SharedVars
import discord
import bot_backend

class SMP(commands.Cog):
    def __int__(self, bot: commands.Bot):
        self.bot = bot

    joinlink_cmd_grp = app_commands.Group(name="joinlink", description="Commands for the server's Minecraft server's join link")

    @joinlink_cmd_grp.command(name="set", description="Set the server's join link")
    @SharedVars.Config.is_mod_or_admin()
    async def set_joinlink(self, interaction: discord.Interaction):
        if interaction.guild_id:
            await interaction.response.send_modal(JoinLinkModal())

    @joinlink_cmd_grp.command(name="check", description="Check what the server's server link is")
    async def get_joinlink(self, interaction: discord.Interaction):
        if interaction.guild_id:
            data = bot_backend.check_join_links(guild_id=interaction.guild_id)

            if data is None:
                await interaction.response.send_message(embed=BotEmbeds.error_embed(error_message="No join links found for this server!"), ephemeral=True)
                return

            java_link, bedrock_link, bedrock_port, embed_title, embed_desc = data

            await interaction.response.send_message(
                embed=BotEmbeds.ip_embed(
                    embed_title=embed_title or "Check out our Minecraft Server!",
                    java_link=java_link,
                    bedrock_link=bedrock_link,
                    bedrock_port=bedrock_port,
                    embed_desc=embed_desc,
                )
            )
        else:
            await interaction.response.send_message("This command can only be run on a server!")
            return
    
    @joinlink_cmd_grp.command(name="remove", description="Remove the join links configured for this server")
    @SharedVars.Config.is_mod_or_admin()
    async def remove_joinlinks(self, interaction: discord.Interaction):
        if interaction.guild_id:
            bot_backend.remove_join_links(guild_id=interaction.guild_id)

            await interaction.response.send_message(embed=BotEmbeds.succsess_embed("Removed server's join links!"))
        else:
            await interaction.response.send_message("This command can only be run on a server!")
            return

    # @app_commands.command(name="smpstatus", description="View the status of the SMP")
    # async def smpstatus(self, interaction: Interaction):
    #     await interaction.response.defer()

    #     try:
    #         server = await JavaServer.async_lookup(SharedVars.smp_link)
    #         status = await server.async_status()


    #         eb = BotEmbeds.smp_embed(latency=round(status.latency), online_players=status.players.online)
    #     except Exception as e:
    #         if "[Errno 104] Connection reset by peer" in str(e) or isinstance(e, ConnectionResetError):
    #             eb = BotEmbeds.smp_error_embed(str(e))
    #             print(f"Failed to send: \"{e}\"")

    #             eb.add_field(
    #                 name="Try running the command again...",
    #                 value=""
    #             )
    #         else:
    #             print(f"Failed to send: \"{e}\"")
    #             eb = BotEmbeds.smp_error_embed(str(e))

    #     await interaction.followup.send(embed=eb, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SMP(bot))
