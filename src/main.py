import discord
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
DEV_GUILD_ID = int(str(getenv("DEV_GUILD_ID"))) # PyCharm is really strict with types for some reason
dev_guild = discord.Object(id=DEV_GUILD_ID)