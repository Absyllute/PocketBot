from discord import ui, TextStyle 
import discord

class EmbedBuilderModal(ui.Modal, title="Create a custom embed"):

    embed_title = ui.TextInput(
        label="Embed title",
        placeholder="Enter announcement title here...",
        required=True,
        max_length=64
    )

    embed_desc = ui.TextInput(
        label="Description (Markdown supported)",
        placeholder="Type your message here...",
        required=True,
        max_length=1024,
        style=TextStyle.paragraph
    )

    embed_ping = ui.TextInput(
        label="Members to ping (Optional)",
        placeholder="@everyone, @here, or Role ID",
        required=False,
        max_length=50
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        eb_ping = self.embed_ping.value if self.embed_ping.value else None
        
        eb = discord.Embed(
            title=self.embed_title.value,
            description=self.embed_desc.value,
            color=0x73d01e
        )

        eb.set_footer(
            icon_url=interaction.user.display_avatar.url,
            text=f"Posted by: {interaction.user.display_name}"
        )

        if isinstance (interaction.channel, (discord.TextChannel, discord.VoiceChannel)):
            await interaction.channel.send(embed=eb)
            await interaction.response.defer(thinking=False)
            await interaction.channel.send(f"||{eb_ping}||")

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message(f"Failed to send embed: {error}", ephemeral=True)
