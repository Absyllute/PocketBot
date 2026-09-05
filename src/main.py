import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
DEV_GUILD_ID = int(str(getenv("DEV_GUILD_ID"))) # PyCharm is really strict with types for some reason
dev_guild = discord.Object(id=DEV_GUILD_ID)

customIntents = discord.Intents.default()
customIntents.message_content = True

class BotClient(commands.Bot):
    def __init__(self, intents: discord.Intents):
        super().__init__(command_prefix='$', intents=customIntents)

    async def setup_hook(self):
        await self.load_extension("cogs.utils_cog")
        await self.load_extension("cogs.moderation_cog")
        await self.load_extension("cogs.smp_cog")

        self.tree.copy_global_to(guild=dev_guild)
        synced = await self.tree.sync(guild=dev_guild)

        print(f"Synced {len(synced)} slash command(s)")

    async def on_ready(self):
        print(f"Logged in as {self.user}")

client = BotClient(intents=customIntents)
client.run(str(TOKEN))