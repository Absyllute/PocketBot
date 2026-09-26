import discord
from discord import ui
from utils.embeds import BotEmbeds

class LogSenderModal(ui.Modal, title = "Send your logs"):

    eb_title = ui.TextInput(
        label="Title",
        placeholder="Crashed at 67%!",
        required=False
    )

    eb_desc = ui.TextInput (
        label="Logs:",
        placeholder="Paste your logs here!",
        style=discord.TextStyle.paragraph,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        eb = BotEmbeds.logs_embed(
            title=self.eb_title.value,
            desc=f"```{self.eb_desc.value}```"
        )
        await interaction.response.send_message(embed=eb)