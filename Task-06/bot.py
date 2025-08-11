import os
import json
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents , help_command = None)

@bot.event
async def on_ready():
    print(f' ✅ Online : {bot.user.name}')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Available Commands",color=0x1DB954)
    embed.add_field(name="🎵 **/lyrics**",value="Get the lyrics of a song.\n**Format:** `/lyrics artist - song name`",inline=False)
    embed.add_field(name="🎼 **/track**",value="Get details about the track \n**Format:** `/track artist - song name`",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def lyrics(ctx, *, input1):
    inp = input1.split("-", 1)
    artist = inp[0].strip()
    song = inp[1].strip()

    url = f"https://lrclib.net/api/search?track_name={song}&artist_name={artist}"
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            data = await r.json()

    songinfo = data[0]
    line = songinfo.get("plainLyrics")
    line = line[:500] 

    embed = discord.Embed(title=f"**🎵 {song} by {artist}**", color=0x1DB954)
    embed.add_field(name="", value=line, inline=False)
    await ctx.send(embed=embed)

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

@bot.command()
async def playlist(ctx, action=None, *, song=None):
    with open("playlist.json", "r") as f:
        playlists = json.load(f)
    user_id = str(ctx.author.id)
    if action == "add":
        if user_id not in playlists:
            playlists[user_id] = []
        playlists[user_id].append(song)
        with open("playlist.json", "w") as f:
            json.dump(playlists, f)
        await ctx.send(f"added `{song}` to your playlist")

    elif action == "remove":
        user_id in playlists and song in playlists[user_id]
        playlists[user_id].remove(song)
        with open("playlist.json", "w") as f:
            json.dump(playlists, f)
        await ctx.send(f"removed `{song}` from your playlist")
    elif action == "view":
        text = ""
        counter = 1
        for s in playlists[user_id]:
            text += f"{counter}. {s}\n"
            counter += 1
        await ctx.send(f"your playlist:\n{text}")
    elif action == "clear":
        playlists[user_id] = []
        with open("playlist.json", "w") as f:
            json.dump(playlists, f)
        await ctx.send("cleared your playlist")

load_dotenv() 
token = os.getenv("TOKEN")
bot.run(token)