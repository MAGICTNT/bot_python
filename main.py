import discord
from discord.ext import commands
from config import MY_CONFIG
from commande.embed import create_embed

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

@bot.command()
async def init_embed(ctx):
    # Utilisation de la fonction create_embed pour créer l'embed
    my_embed = create_embed("Hello!", f"Bonjour, {ctx.author.mention}!", discord.Color.blue())
    
    # Ajout d'un champ dans l'embed
    my_embed.add_field(name="Bienvenue", value="Bienvenue sur notre serveur Discord!")
    
    # Envoi de l'embed
    await ctx.send(embed=my_embed)


bot.run(MY_CONFIG['token'])