import discord
from discord.ext import commands
import database


class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx):
        items = database.get_shop_items()
        lines = ["**Grand Line Shop:**"]
        for item in items:
            lines.append(f"• **{item['name']}** (`{item['item_id']}`) - `{item['cost']}` Berries\n  {item['effect']}")

        await ctx.send("\n".join(lines))

    @commands.command()
    async def buy(self, ctx, *, item_id: str = None):
        if not item_id:
            await ctx.send("Usage: `!buy <item_id>` (check `!shop` for items)")
            return

        database.get_pirate(ctx.author.id, ctx.author.display_name)
        success, msg = database.buy_shop_item(ctx.author.id, item_id.strip())
        await ctx.send(msg)

    @commands.command(name="inventory", aliases=["inv"])
    async def inventory(self, ctx, member: discord.Member = None):
        target = member or ctx.author
        if target.bot:
            await ctx.send("Bots do not have inventories.")
            return

        database.get_pirate(target.id, target.display_name)
        items = database.get_inventory(target.id)

        if not items:
            await ctx.send(f"{target.display_name}'s inventory is empty.")
            return

        lines = [f"**{target.display_name}'s Inventory:**"]
        for item in items:
            lines.append(f"• **{item['name']}** [{item['status']}] - {item['effect']}")

        await ctx.send("\n".join(lines))


async def setup(bot):
    await bot.add_cog(Shop(bot))
