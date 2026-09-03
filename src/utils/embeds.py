import discord
from discord import Embed
from pathlib import Path
import utils.shared_vars as shared_vars
from mcstatus import JavaServer

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ICON_PATH = BASE_DIR / "assets" / "images" / "PH_icon.png"
DEV_ICON_PATH = BASE_DIR / "assets" / "images" / "absyllute.jpg"


class BotEmbeds:

    @staticmethod
    def smp_error_embed() -> Embed:
        eb = Embed(
            title="Error",
            description="An error occoured when running this command"
        )

        return eb

    @staticmethod
    def smp_embed(srv: JavaServer) -> Embed:
        eb = Embed(
            title="PocketCraft SMP Status",
            color=shared_vars.primary_colour
        )

        latency = srv.ping()

        eb.add_field(
            name="Ping",
            value=f"`{latency}ms`"
        )

        return eb

    @staticmethod
    def ip_embed() -> Embed:
        eb = Embed(
            title="PocketCraft SMP",
            description="Early closed beta for server memebers",
            color=shared_vars.primary_colour
        )

        eb.add_field(
            name="Java Edition:",
            value="`play.pocketcraft-smp.online`",
            inline=True
        )

        eb.add_field(
            name="Bedrock Edition:",
            value="`bedrock.pocketcraft-smp.online` \n Port: `17506`",
            inline=True
        )

        eb.add_field(
            name="Note:",
            value="The ping is really high at the moment, bear with us",
            inline=False
        )

        eb.set_footer(
            text="SMP run by Absyllute"
        )

        return eb


    @staticmethod
    def ping_embed(latency: int) -> Embed:
        embed = discord.Embed(
            title='**Pong! PocketBot is online!!**',
            description=f'**Round Latency:** `{latency}ms`',
            color=shared_vars.primary_colour
        )

        embed.set_footer(text="Bot by @Absyllute")

        return embed
    @staticmethod
    def about_embed(ver: str) -> tuple[Embed, discord.File, discord.File]:
        bot_icon = discord.File(ICON_PATH, filename="ico.png")
        dev_icon = discord.File(DEV_ICON_PATH, filename="absyllute.png")
        eb = discord.Embed(
            title="PocketBot",
            description="The official bot for the PocketHost Discord server",
            color=shared_vars.primary_colour
        )

        eb.add_field(name="Version", value=f"{ver} | Updated: 29 August 2026")
        eb.add_field(name="Framework", value="discord.py", inline=False)

        eb.set_footer(text="Bot developed by @absyllute", icon_url="attachment://absyllute.png")
        eb.set_thumbnail(url="attachment://ico.png")

        return eb, bot_icon, dev_icon