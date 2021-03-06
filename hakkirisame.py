import os
import random
import discord
from discord.ext import commands

hakkiri = commands.Bot(command_prefix='>>')


# Events
@hakkiri.event
async def on_ready():
    print('Bot is online')
    status = [
        'traque de massa', 'dark souls 3 e peidando pro midir',
        'lolis no porão', 'bola na pracinha'
    ]
    await hakkiri.change_presence(activity=discord.Game(random.choice(status)))


# Commands
@hakkiri.command(aliases=['ajuda'])
async def _help(ctx):
    await ctx.send(
        'lista de comandos:\n>>ping\n>>responda (pergunta)\n>>dado\n>>a\n>>momentocria'
    )


@hakkiri.command()
async def ping(ctx):
    pongs = [
        'pong no teu bong?????', 'pong o caralho te fode fidaputa',
        'pong é massa'
    ]
    await ctx.send(f'{random.choice(pongs)}')


@hakkiri.command(aliases=['pergunte', 'responda'])
async def responda(ctx, *, question):
    respostas = [
        'sim', 'com ctz', 'se pa', 'sla porra', 'é 6', 'claro que n mamao',
        'te fode fidaputa', 'yametekudastop'
    ]
    await ctx.send(f'{random.choice(respostas)}')


@hakkiri.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)


@hakkiri.command()
async def dado(ctx):
    dados = ['1', '2', '3', '4', '5', 'tu tem dado em casa?']
    await ctx.send(f'{random.choice(dados)}')

@hakkiri.command()
async def a(ctx):
    shark_facts = [
        'Carnívoro absoluto, ele caça peixes pequenos ou os grandes que já estão moribundos. Nunca para de nadar e gasta muita energia. Por isso, tem digestão super rápida e precisar comer constantemente.',
        'O tubarão é míope.',
        'A pele de tubarão tem uma textura semelhante a uma lixa. Tubarões não podem ser boing boing pois eles são hidrodinâmicos devido a essa pele.',
        'Tubarões perdem 20.000 dentes durante a sua vida. Isso é mais ou menos 20.000 bananas.',
        'a',
        'O Tubarão-Martelo tem uma cabeça no formato de martelo. A sua comida favorita são arraias. Eles provavelmente chupam elas feito um sacolé.',
        'Um megalodon tem um tamanho equivalente a 140 bananas. 140 bananas de dentes e poder.',
    ]
    await ctx.send(f'{random.choice(shark_facts)}')


hakkiri.run(os.environ['DISCORD_TOKEN'])
