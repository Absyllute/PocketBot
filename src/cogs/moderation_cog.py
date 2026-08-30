import discord
from discord import app_commands
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    purge_group = app_commands.Group(name="purge", description="Mass delete messages, with filters")

    # --- --- --- Purge Any --- --- --- #
    @purge_group.command(name="any", description="Mass delete messages, regardless of the sender. Limit: 100")
    async def purge_any(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            deleted = await interaction.channel.purge(limit=amount)

            await interaction.followup.send(f"Deleted {len(deleted)} messages!")
        else:
            await interaction.followup.send("Unable to purge messages in this channel", ephemeral=True)

    # --- --- --- Purge Human --- --- --- #
    @purge_group.command(name="human", description="Mass delete messages made by humans (non-bots). Limit: 100")
    async def purge_human(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)
        count = 0

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            def is_human(msg: discord.Message) -> bool:
                nonlocal count
                
                if not msg.author.bot and count < amount:
                    count += 1
                    return True
                else:
                    return False

            messages_deleted = await interaction.channel.purge(limit=100, check=is_human)

            await interaction.followup.send(f"Deleted {len(messages_deleted)} human messages!", ephemeral=True)
        else:
            await interaction.followup.send("Unable to purge messages in this channel")

    # --- --- --- Purge Bots --- --- --- #
    @purge_group.command(name="bot", description="Mass delete messages made by bots (clankers). Limit: 100")
    async def purge_bot(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)
        count = 0

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            def is_bot(msg: discord.Message) -> bool:
                nonlocal count

                if msg.author.bot and count < amount:
                    count += 1
                    return True
                else:
                    return False

            messages_deleted = await interaction.channel.purge(limit=100, check=is_bot)

            await interaction.followup.send(f"Deleted {len(messages_deleted)} messages!")
        else:
            await interaction.followup.send("Unable to purge this channel type!")

    # --- --- --- Purge User --- --- --- #
    @purge_group.command(name="user", description="Delete messages only from a certain user. Limit: 100")
    async def purge_user(self, interaction: discord.Interaction, user: discord.Member, amount: int):
        await interaction.response.defer(ephemeral=True)
        count = 0

        if isinstance(interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            def isTarget(msg: discord.Message) -> bool:
                nonlocal count

                if msg.author.id == user.id and count < amount:
                    count += 1
                    return True
                else:
                    return False

            messages_deleted = await interaction.channel.purge(limit=100, check=isTarget)

            await interaction.followup.send(f"Deleted {len(messages_deleted)} messages from {user}")
        else:
            await interaction.followup.send("Unable to purge this channel type")

async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot=bot))