import random
import discord
from discord.ext import commands

hakkiri = commands.Bot(command_prefix = '$')

# Events
@hakkiri.event
async def on_ready():
    print('Bot is online')
    await hakkiri.change_presence(activity=discord.Game('6 castanhas no quarto de jayb'))

# Commands
@hakkiri.command(aliases=['ajuda'])
async def _help(ctx):
    await ctx.send('lista de comandos aqui: https://github.com/HakkouV/Hakkirisame')
@hakkiri.command()
async def ping(ctx):
    pongs = ['pong no teu bong?????', 'pong o caralho te fode fidaputa', 'pong é massa']
    await ctx.send(f'{random.choice(pongs)}')

@hakkiri.command(aliases=['6ball', 'responda'])
async def _6ball(ctx, *, question):
    respostas = ['sim', 'com ctz', 'se pa', 'sla porra', 'é 6', 'claro que n mamao', 'te fode fidaputa']
    await ctx.send(f'{random.choice(respostas)}')

@hakkiri.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)
    
@hakkiri.command()
async def dado(ctx):
    dados = ['1', '2', '3', '4', '5', 'tu tem dado em casa?']
    await ctx.send(f'{random.choice(dados)}')


# you should put your discord bot token here, removed for obvious reasons
hakkiri.run('...')
