import discord
from discord.ext import commands
from discord import app_commands
from utils.embeds import BotEmbeds
from modals.embed_builder_modal_ import EmbedBuilderModal
import utils.shared_vars as SharedVars
import rusty_core

class Config(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    modrole_cmd_grp  = app_commands.Group(name="modrole", description="Commands for adding staff members for staff-only commands")
    joinlink_cmd_grp = app_commands.Group(name="joinlink", description="Commands for the server's Minecraft server's join link")

    @joinlink_cmd_grp.command(name="set", description="Set the server's join link")
    @SharedVars.Config.is_mod_or_admin()
    async def set_joinlink(self, interaction: discord.Interaction, url: str):
        if interaction.guild_id:
            # rusty_core.set_join_link(guild_id=interaction.guild_id, url=url)

            await interaction.response.send_message(embed=BotEmbeds.succsess_embed(success_message="Set server join link successfully!"))
    
    ### --- ### Modrole config ### --- ###
    @modrole_cmd_grp.command(name="add", description="Adds a role to be able run eleveted commands")
    @SharedVars.Config.is_mod_or_admin()
    async def add_modrole(self, interaction: discord.Interaction, role: discord.Role):
        if isinstance (interaction.user, discord.Member):
            if interaction.user.guild_permissions.administrator and interaction.guild_id:
                SharedVars.Config.mod_roles.add(role.id)
                rusty_core.add_modrole(guild_id=interaction.guild_id, role_id=role.id)
                await interaction.response.send_message(embed=BotEmbeds.succsess_embed(success_message=f"Added {role.mention} to the list of modroles!"))
            else:
                await interaction.response.send_message(embed=BotEmbeds.error_embed("Only people with the Administrator permission can run this command!"), ephemeral=True)

    @modrole_cmd_grp.command(name="remove", description="Removes a role from the modrole group")
    @SharedVars.Config.is_mod_or_admin()
    async def remove_modrole(self, interaction: discord.Interaction, role: discord.Role):
        if isinstance (interaction.user, discord.Member):
            if interaction.user.guild_permissions.administrator and interaction.guild_id:
                SharedVars.Config.mod_roles.discard(role.id)
                rusty_core.remove_modrole(guild_id=interaction.guild_id, role_id=role.id)
                await interaction.response.send_message(embed=BotEmbeds.succsess_embed(f"Removed {role.mention} from the list of modroles!"))
            else:
                await interaction.response.send_message(embed=BotEmbeds.error_embed("Only people with the Administrator permission can run this command!"), ephemeral=True)

    @modrole_cmd_grp.command(name="list", description="List all roles that are part of the modrole group")
    @SharedVars.Config.is_mod_or_admin()
    async def list_modroles(self, interaction: discord.Interaction):
        if isinstance(interaction.user, discord.Member) and interaction.guild_id:
            modroles: list[int] = rusty_core.check_modroles(guild_id=interaction.guild_id)
            role_index: int = 1
            desc: str = ""

            for role in modroles:
                desc += f"Modrole {role_index}: <@&{role}>\n"
                role_index += 1

            embed = BotEmbeds.info_embed(title="Modroles:", desc=desc)
            await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Config(bot=bot))

