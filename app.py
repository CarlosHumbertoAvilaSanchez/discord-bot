import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from services import music


load_dotenv()
API_KEY = os.getenv("API_KEY")
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.load_extension("services.music")
    print("Bot is ready")


client.run(API_KEY)
