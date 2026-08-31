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

    embed_thumb = ui.TextInput(
        label="Thumbnail URL (Optional)",
        placeholder="Image link here...",
        required=False
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        eb = discord.Embed(
            title=self.embed_title.value,
            description=self.embed_desc.value,
        )

        if self.embed_thumb.value:
            eb.set_thumbnail(url=self.embed_thumb.value)

        eb.set_footer(
            icon_url=interaction.user.display_avatar.url,
            text=f"Posted by: {interaction.user.mention}"
        )

        await interaction.response.send_message(embed=eb)

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message(f"Failed to send embed: {error}", ephemeral=True)
