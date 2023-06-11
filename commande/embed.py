import discord

def create_embed(title, description, color):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    return embed