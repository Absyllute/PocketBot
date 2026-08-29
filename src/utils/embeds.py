import discord
from pathlib import Path

PRIMARY_COLOUR = discord.Color.brand_green()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ICON_PATH = BASE_DIR / "assets" / "images" / "PH_icon.png"
DEV_ICON_PATH = BASE_DIR / "assets" / "images" / "absyllute.jpg"


class BotEmbeds:
    @staticmethod
    def ping_embed(latency: int) -> discord.Embed:
        embed = discord.Embed(
            title='**Pong! PocketBot is online!!**',
            description=f'**Round Latency:** `{latency}ms`',
            color=PRIMARY_COLOUR
        )

        embed.set_footer(text="Bot by @Absyllute")

        return embed
    @staticmethod
    def about_embed(ver: str) -> tuple[discord.Embed, discord.File, discord.File]:
        bot_icon = discord.File(ICON_PATH, filename="ico.png")
        dev_icon = discord.File(DEV_ICON_PATH, filename="absyllute.png")
        eb = discord.Embed(
            title="PocketBot",
            description="The official bot for the PocketHost Discord server",
            color=PRIMARY_COLOUR
        )

        eb.add_field(name="Version", value=f"{ver} | Updated: 29 August 2026")
        eb.add_field(name="Framework", value="discord.py", inline=False)

        eb.set_footer(text="Bot developed by @absyllute", icon_url="attachment://absyllute.png")
        eb.set_thumbnail(url="attachment://ico.png")

        return eb, bot_icon, dev_icon