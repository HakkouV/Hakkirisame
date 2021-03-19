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
    await ctx.send('lista de comandos:\n>>ping\n>>6ball\n>>clear\n>>dado\n>>a')


@hakkiri.command()
async def ping(ctx):
    pongs = [
        'pong no teu bong?????', 'pong o caralho te fode fidaputa',
        'pong é massa'
    ]
    await ctx.send(f'{random.choice(pongs)}')


@hakkiri.command(aliases=['6ball', 'responda'])
async def _6ball(ctx, *, question):
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
async def elitista(ctx):
    anime = [
        "Evangelion", "Tatami Galaxy", "Legend of the Galactic Heroes",
        "Serial Experiments Lain", "Ashita no Joe", "NHK ni Youkoso",
        "Texhnolyze", "Cowboy Bebop", "Gundam", "FLCL", "Macross", "Berserk",
        "Kaiji", "Haibane Renmei", "Princess Tutu", "Ergo Proxy",
        "Angel's Egg", "Area 88", "Detective Conan", "The End of Evangelion",
        "Sketchbook: Full Color's", "Fullmetal Alchemist: Brotherhood",
        "Sayonara Zetsubou Sensei", "Oyasumi Punpun", "Akage no Anne",
        "Sword Art Online", "Chaves", "Avatar", "Monogatari", "Steins;Gate",
        "Planetes", "Devilman Crybaby", "Ping Pong The Animation", "ARIA",
        "Monster"
    ]
    temas = [
        "a animação.", "a trama.", "o enredo.", "a direção.",
        "os subtemas escondidos.", "o real significado da obra.",
        "o seu impacto no mundo dos animes/mangás.", "as tetas da waifu."
    ]
    adjetivo = [
        "gordo", "inseguro", "maluco", "magrelo", "branco", "preto", "pobre",
        "verme", "nerdola", "cria", "channer", "redditor"
    ]
    crise = [
        "depressão", "esquizofrenia", "ansiedade", "retardo mental",
        "síndrome de down", "autismo", "burro", "anorexia", "bulimia"
    ]
    metodos = [
        "um blog pessoal onde ele escreve resenhas e reviews sobre animes.",
        "um canal no youtube.", "uma conta no twitter sobre animes.",
        "shitposting no server do discord favorito dele.",
        "se fingir de mulher no MAL.", 'um "se liga no LULZ" não ironicamente.'
    ]
    await ctx.send(
        f'{"Um elitista com o anime/mangá favorito sendo" random.choice(anime) 
        "que discute diariamente sobre" random.choice(temas) 
        ". Mas ele na verdade é um" random.choice(adjetivo) 
        "com" random.choice(crise) 
        "e tenta esconder através de" random.choice(metodos)}'
    )

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
