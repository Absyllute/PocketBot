import discord
from discord.ext import commands
from discord import app_commands
from utils.embeds import BotEmbeds
from modals.embed_builder_modal_ import EmbedBuilderModal
import utils.shared_vars as SharedVars
import rusty_core

class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    embed_cmd_grp = app_commands.Group(name="embed", description="Commands for making and edit pretty embeds")
    modrole_cmd_grp = app_commands.Group(name="modrole", description="Commands for adding staff members for staff-only commands")

    ### --- ### Require user to be in the modrole group ### --- ###
    @embed_cmd_grp.command(name="builder", description="Create an embed from scratch")
    @SharedVars.Config.is_mod_or_admin()
    async def builder(self, interaction: discord.Interaction):
        await interaction.response.send_modal(EmbedBuilderModal())

    @modrole_cmd_grp.command(name="add", description="Adds a role to be able run eleveted commands")
    @SharedVars.Config.is_mod_or_admin()
    async def add_modrole(self, interaction: discord.Interaction, role: discord.Role):
        if isinstance (interaction.user, discord.Member):
            if interaction.user.guild_permissions.administrator:
                if interaction.guild_id is not None:
                    SharedVars.Config.mod_roles.add(role.id)
                    rusty_core.add_modrole(guild_id=interaction.guild_id, role_ids=list(SharedVars.Config.mod_roles))
                    await interaction.response.send_message(embed=BotEmbeds.succsess_embed(success_message=f"Added {role.mention} to the list of modroles!"))
            else:
                await interaction.response.send_message(embed=BotEmbeds.error_embed("Only people with the Administrator permission can run this command!"), ephemeral=True)

    @modrole_cmd_grp.command(name="remove", description="Removes a role from the modrole group")
    @SharedVars.Config.is_mod_or_admin()
    async def remove_modrole(self, interaction: discord.Interaction, role: discord.Role):
        if isinstance (interaction.user, discord.Member):
            if interaction.user.guild_permissions.administrator:
                SharedVars.Config.mod_roles.remove(role.id)
                await interaction.response.send_message(embed=BotEmbeds.succsess_embed(f"Removed {role.mention} from the list of modroles!"))
            else:
                await interaction.response.send_message(embed=BotEmbeds.error_embed("Only people with the Administrator permission can run this command!"), ephemeral=True)

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