import random
import aiohttp
from discord.ext import commands

FALLBACK_INTEL = [
    "Gomu Gomu no Mi (Nika): Mythical Zoan giving rubber powers and freedom.",
    "Mera Mera no Mi: Logia fruit that lets the user control fire.",
    "Ope Ope no Mi: Paramecia fruit creating surgical ROOMs.",
    "Gura Gura no Mi: Paramecia fruit creating massive shockwaves.",
    "Gol D. Roger Bounty: 5,564,800,000 Berries (Pirate King)",
    "Whitebeard Bounty: 5,046,000,000 Berries (Strongest Man)",
    "Kaido Bounty: 4,611,100,000 Berries (King of the Beasts)",
    "Shanks Bounty: 4,048,900,000 Berries (Red Hair Emperor)",
    "Buggy Bounty: 3,189,000,000 Berries (Cross Guild Leader)",
    "Laugh Tale: The legendary final island where the One Piece is located."
]


class LogPose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="logpose", aliases=["intel"])
    async def logpose(self, ctx):
        try:
            url = "https://api.api-onepiece.com/v2/fruits/en"
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=2)) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if isinstance(data, list) and len(data) > 0:
                            fruit = random.choice(data)
                            name = fruit.get("name") or fruit.get("roman_name")
                            desc = fruit.get("description", "A mysterious Devil Fruit.")
                            await ctx.send(f"**Log Pose:** **{name}**\n{desc}")
                            return
        except Exception:
            pass

        await ctx.send(f"**Log Pose:** {random.choice(FALLBACK_INTEL)}")


async def setup(bot):
    await bot.add_cog(LogPose(bot))
