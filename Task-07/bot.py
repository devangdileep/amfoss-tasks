import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import database

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is online")

async def main():
    database.init_db()

    await bot.load_extension("commands.economy")
    await bot.load_extension("commands.shop")
    await bot.load_extension("commands.logpose")
    await bot.load_extension("commands.raid")

    

    token = os.getenv("DISCORD_TOKEN")
    await bot.start(token)

asyncio.run(main())
