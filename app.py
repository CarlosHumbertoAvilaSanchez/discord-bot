import discord
from discord.ext import commands
from services import music

API_KEY = "MTIxMzg5ODQyODQyNjM1NDc2MA.GjbDoS.UWcIZiSoYPwxw-jNGRBaKYsTjGpnmhOaEnoNmY"
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.load_extension("services.music")
    print("Bot is ready")


client.run(API_KEY)
