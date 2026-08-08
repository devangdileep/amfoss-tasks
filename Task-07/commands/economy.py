import random
import discord
from discord.ext import commands
import database


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bounty(self, ctx, member: discord.Member = None):
        target = member or ctx.author
        if target.bot:
            await ctx.send("Bots do not have a bounty.")
            return

        pirate = database.get_pirate(target.id, target.display_name)
        total = pirate["wallet"] + pirate["bank"]

        msg = (
            f"**{target.display_name}'s Bounty**\n"
            f"Wallet: `{pirate['wallet']}` Berries\n"
            f"Bank: `{pirate['bank']}` Berries\n"
            f"Total: `{total}` Berries"
        )
        await ctx.send(msg)

    @commands.command()
    async def setsail(self, ctx):
        database.get_pirate(ctx.author.id, ctx.author.display_name)
        loot = random.randint(500, 1500)
        success, msg = database.claim_daily_berries(ctx.author.id, loot)
        await ctx.send(msg)

    @commands.command()
    async def trade(self, ctx, recipient: discord.Member, amount: int):
        if recipient.bot:
            await ctx.send("Cannot trade with bots.")
            return

        database.get_pirate(ctx.author.id, ctx.author.display_name)
        database.get_pirate(recipient.id, recipient.display_name)

        success, msg = database.trade_berries(ctx.author.id, recipient.id, amount)
        if success:
            await ctx.send(f"Transferred `{amount}` Berries to **{recipient.display_name}**.")
        else:
            await ctx.send(msg)

    @commands.command(name="worstgeneration", aliases=["top"])
    async def worstgeneration(self, ctx):
        top_list = database.get_top_pirates(5)
        if not top_list:
            await ctx.send("No pirates registered yet.")
            return

        lines = []
        for idx, p in enumerate(top_list, 1):
            lines.append(f"{idx}. {p['username']} - `{p['total']}` Berries")

        await ctx.send("\n".join(lines))


async def setup(bot):
    await bot.add_cog(Economy(bot))
