import os
import aiohttp
import discord
import musicbrainzngs
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents , help_command = None)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Available Commands",color=0x1DB954)
    embed.add_field(name="🎵 **/lyrics**",value="Get the lyrics of a song.\n**Format:** `/lyrics artist - song name`",inline=False)
    embed.add_field(name="🎼 **/track**",value="Get details about the track \n**Format:** `/track artist - song name`",inline=False)
    await ctx.send(embed=embed)

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


@bot.command()
async def track(ctx, *, input1):
    l = input1.split('-', 1)
    artist = " ".join(l[0].split())
    song = " ".join(l[1].split())
    url = f'https://musicbrainz.org/ws/2/recording/?query=artist:"{artist}" AND recording:"{song}"&fmt=json'
    async with aiohttp.ClientSession() as search:
        async with search.get(url) as responce:
            data = await responce.json()

    track_info = data["recordings"][0]
    title = track_info.get("title", "Unknown Title")
    artist_name = track_info["artist-credit"][0]["name"]
    time_ms = track_info.get("length", 0)
    time_min = time_ms // 60000
    album = track_info["releases"][0]["title"] 
    date = track_info["releases"][0].get("date", "Unknown Date")

    embed = discord.Embed(title=f"🎵 {title} — {artist_name}",color=0x1DB954)
    embed.add_field(name="**📀 Album**", value=album, inline=False)
    embed.add_field(name="**⏱️ Length**", value=f"{time_min} min", inline=False)
    embed.add_field(name="**📅 Release Date**", value=date, inline=False)
    await ctx.send(embed=embed)


load_dotenv() 
token = os.getenv("TOKEN")
bot.run(token)