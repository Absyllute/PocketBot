import discord
from discord.types import embed

PRIMARY_COLOUR = discord.Color.brand_green()

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