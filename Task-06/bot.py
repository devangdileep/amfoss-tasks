import os
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

load_dotenv() 
token = os.getenv("TOKEN")
bot.run(token)