from discord import ui, TextStyle
import discord
import rusty_core

class JoinLinkModal(ui.Modal, title="Customise your server"):
    embed_title = ui.TextInput(
        label="Embed Title",
        placeholder="PocketHost SMP"
    )

    embed_desc = ui.TextInput(
        label="Description (Markdown Supported :)",
        placeholder="The **Official** SMP for the PocketHost Discord server.",
        style=TextStyle.paragraph
    )

    java_link_title = ui.TextInput(
        label="Java Link Title:",
        placeholder="Java Edition (1.21.11+)"
    )

    java_link = ui.TextInput(
        label="Java Join Link",
        placeholder="play.examplesmp.gg"
    )

    bedrock_link_title = ui.TextInput(
        label="Bedrock Join Title",
        placeholder="Bedrock Edtion (26.1+):"
    )

    bedrock_link = ui.TextInput(
        label="Bedrock Join Link",
        placeholder="play.bedrockers.gg"
    )

    bedrock_port = ui.TextInput(
        label="Bedrock Port",
        placeholder="12367",
        style=TextStyle.short
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        if not interaction.guild_id:
            await interaction.response.send_message("This command can only be run on a server!")
            return

        port_str = self.bedrock_port.value.strip() # strip white-space
        port_val = int(port_str) if port_str.isdigit() else 0

        rusty_core.setup_join_link(
            embed_title=self.embed_title.value,
            embed_desc=self.embed_desc.value,
            guild_id=interaction.guild_id,
            java_link=self.java_link.value,
            bedrock_link=self.bedrock_link.value,
            bedrock_port=port_val
        )