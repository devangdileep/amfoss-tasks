import os
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents , help_command = None)

@bot.command()
async def help(ctx):
    embed = discord.Embeded(title = "Help Commands" , description = "Under Construction")
    await ctx.send(embed)

@bot.command()
async def lyrics(ctx, *, input1):
    l = input1.split('-', 1)
    artist = l[0].strip()
    song = l[1].strip()
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    async with aiohttp.ClientSession() as searching:
        async with searching.get(url) as data:
            data = await data.json()
    lyrics = data.get("lyrics")
    await ctx.send(lyrics)


load_dotenv() 
token = os.getenv("TOKEN")
bot.run(token)