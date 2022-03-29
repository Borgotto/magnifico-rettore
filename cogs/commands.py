from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands loaded!")


async def setup(bot):
    await bot.add_cog(Commands(bot))