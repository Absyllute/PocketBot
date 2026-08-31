from discord import ui, TextStyle 
import discord

class EmbedBuilderModal(ui.Modal, title="Create a custom embed"):

    embed_title = ui.TextInput(
        label="Embed Title",
        placeholder="Title, Keep it short and descriptive",
        required=True,
        max_length=64
    )

    embed_desc = ui.TextInput(
        label="Content / Description",
        placeholder="Hello World! The content of your embed goes here. Markdown supported :)",
        required=True,
        max_length=1024,
        style=TextStyle.paragraph
    )

    embed_thumb = ui.TextInput(
        label="Image URL for the embed thumbnail (Optional)",
        placeholder="https://example.com/image.png",
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
