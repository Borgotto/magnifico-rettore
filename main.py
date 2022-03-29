import os
import asyncio
import discord
from discord.ext import commands


# Try to get the bot token from file, quit if it fails
try:
    with open('token') as file:
        token = file.readline()
except IOError:
    print("Missing token file containing the bot's token")
    quit()

# Create config and cog folders if they don't exist
if not os.path.exists('./config/'):
    os.makedirs('./config/')
if not os.path.exists('./cogs/'):
    os.makedirs('./cogs/')

# Create bot object
bot = commands.Bot(command_prefix="mhh",
                        strip_after_prefix=True,
                        owner_id=289887222310764545,
                        intents=discord.Intents.all())

# Load all .py files from 'cogs' directory
for filename in os.listdir('./cogs'):
    if (filename.endswith('.py')):
        asyncio.run(bot.load_extension(f'cogs.{filename[:-3]}'))

@bot.event
async def on_ready():
    # Set the bot presence status
    await bot.change_presence(status=discord.Status.online)

    # Print a bunch of info about the bot
    print ("\n--------------------------------\n")
    print ("Bot Name:", bot.user.name)
    print ("Bot ID:", bot.user.id)
    print ("discord.py version:", discord.__version__)
    print ("\n--------------------------------\n")

bot.run(token)