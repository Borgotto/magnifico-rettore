from discord.ext import commands


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slash commands loaded!")


async def setup(bot):
    await bot.add_cog(SlashCommands(bot))