import discord
from discord.ext import commands
from config import MY_CONFIG

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def hello(ctx):
    print('Hello command received')
    await ctx.send('Hello, Discord!')

bot.run(MY_CONFIG['token'])