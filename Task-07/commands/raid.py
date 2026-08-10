import random
import discord
from discord.ext import commands
import database


class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def raid(self, ctx, target: discord.Member = None):
        if target is None:
            await ctx.send("Usage: `!raid @username`")
            return

        if target.bot or target.id == ctx.author.id:
            await ctx.send("Invalid target for raid.")
            return

        raider = database.get_pirate(ctx.author.id, ctx.author.display_name)
        defender = database.get_pirate(target.id, target.display_name)

        if raider["wallet"] < 50:
            await ctx.send("You need at least 50 Berries to raid.")
            return

        if defender["wallet"] < 50:
            await ctx.send(f"{target.display_name} has too few Berries to raid.")
            return

        if random.random() < 0.5:
            stolen = max(10, int(defender["wallet"] * 0.20))
            database.update_wallet(target.id, -stolen)
            database.update_wallet(ctx.author.id, stolen)
            await ctx.send(f"Raid Success! You stole `{stolen}` Berries from **{target.display_name}**!")
        else:
            penalty = max(10, int(raider["wallet"] * 0.15))
            database.update_wallet(ctx.author.id, -penalty)
            database.update_wallet(target.id, penalty)
            await ctx.send(f"Raid Failed! You lost `{penalty}` Berries to **{target.display_name}**.")


async def setup(bot):
    await bot.add_cog(Raid(bot))
