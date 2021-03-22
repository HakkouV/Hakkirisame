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
async def momentocria(ctx):
    momentos = [
        'https://clips.twitch.tv/AgileBashfulCarrotJonCarnage-NDYSd4jmhGEDdQa7',
        'https://cdn.discordapp.com/attachments/767932279992483880/767932298158145536/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/767933012398047232/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/767962031428206622/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/769299367479214091/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/769676708324311040/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/769740253266182214/unknown.png',
        'lista atualizada de nicks do killbay:\nkillbay, killb, mushi, retrohead, newi, badapoxos, kupo, mushiguchi, kopoxos, kopungroove, badabing',
        'https://cdn.discordapp.com/attachments/767932279992483880/770028766851760188/unknown.png',
        'https://cdn.discordapp.com/attachments/763976384916881418/769455424582975488/Screenshot_20201024-040056_Discord.jpg',
        'https://cdn.discordapp.com/attachments/767932279992483880/770441354781786152/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/771204323757654016/unknown-31.png',
        'https://cdn.discordapp.com/attachments/638889706465263648/771178711013261362/unknown.png',
        'https://cdn.discordapp.com/attachments/638889706465263648/771178752964821012/unknown.png',
        'discord.gg/cellbit',
        'https://cdn.discordapp.com/attachments/767932279992483880/775932988503359488/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/778307358648434708/IMG_20201117_141716.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/779296793560219648/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/779511260810838036/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/782034503626784768/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/782040472771362836/image0.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/782064648257142804/SPOILER_unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/782653527515725834/Screenshot_7322.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/783118797598752798/Screenshot_20201130-205405_1.png',
        'https://media.discordapp.net/attachments/512721795523280896/754875885747830875/unknown.png',
        'https://cdn.discordapp.com/attachments/548617197287768087/754891316881784862/unknown-1.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/788098018645770260/unknown-47.png',
        'https://cdn.discordapp.com/attachments/764277352162656279/789324877231685642/SPOILER_unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/790044351778258964/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/795006461629300736/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/801199491683188736/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/808379034329153576/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/808379730063523880/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/809253089899053066/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/809588832486817802/unknown.png',
        'https://image.prntscr.com/image/W8axISR8S1Wv2zMYQU7Xow.png',
        'https://image.prntscr.com/image/PQt_mReeSSCUhPK2mpFHHQ.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/812478604998737990/unknown.png',
        'https://clips.twitch.tv/IncredulousSillyHamburgerShazBotstix-7k1YLvR_OM00t41w',
        'https://cdn.discordapp.com/attachments/767932279992483880/820164282510475284/unknown.png',
        'https://cdn.discordapp.com/attachments/767932279992483880/821445520648044584/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/771843532176228363/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/771844565270265866/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/771844589228654612/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/771882686703730708/unknown-535.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/771904535215472671/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/772064597862514688/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/772484246429630475/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/778848894602706954/doi.png',
        'https://media.discordapp.net/attachments/779846470085378102/782783777511571476/image0-3.gif',
        'https://cdn.discordapp.com/attachments/771839206804160523/784434155618041886/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/784434997850669116/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/784435072329580614/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/794413286682132541/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/798057660153987082/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/798104059550760970/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/799865972734820362/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/802712114342395934/20210123_223046.jpg',
        'https://cdn.discordapp.com/attachments/771839206804160523/805589214959763506/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/808024566584573962/dias_sem_o_killb_dar_rage.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/808048400338780210/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/808057751581491210/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/808077544049737728/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/808490391137157170/volta_quando_ler_autor_chines.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/808491018416160818/godoi_transudo.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/809247697655169034/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/809253378977955880/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/810584417474314250/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/812355206339493898/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/812527867065270292/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/814662891831296080/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/816325297837965352/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/817038369565442058/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/820164271308013628/unknown.png',
        'https://cdn.discordapp.com/attachments/771839206804160523/820338597387173930/unknown.png',
        'https://media.discordapp.net/attachments/785709386960994324/785790051560325120/reverse.gif?width=264&height=264',
        'https://images-ext-2.discordapp.net/external/ypfHiJC0VxHzG7EjMnKkYsmyqHbTa6l6JlIAEru5RIM/https/i.imgur.com/VMTAHPg.mp4',
        'https://media.discordapp.net/attachments/764277352162656279/767631513596461056/teaga_e_joun.gif?width=540&height=304',
        'https://images-ext-1.discordapp.net/external/jQXA_qo3Z1VC8F-yTWKr1WADVorjXZ86iThUfGfE2eE/%3Fv%3D1/https/cdn.discordapp.com/emojis/767629174151839775.gif?width=115&height=61',
        'https://media.discordapp.net/attachments/789206612346535936/789620914362908672/criasrindo.gif?width=288&height=216',
        'https://images-ext-1.discordapp.net/external/OYAwb0Rp2OBhBhxDo82Ni5MpJehIjH4c0TgPQEuhkQU/https/media.discordapp.net/attachments/474433118040883217/785686624234242048/reface-2020-11-05-03-00-47.gif?width=193&height=108',
        'https://images-ext-1.discordapp.net/external/ESsSyUJ0BhFZflwtgYMlB1ZSfLmR0wW-JYVXgUmk1FE/https/i.imgur.com/O6SHY9Z.mp4',
        'https://media.discordapp.net/attachments/789206612346535936/794810249571467275/familia.jpg?width=706&height=565', 
        'https://media.discordapp.net/attachments/789206612346535936/798364928225574942/unknown.png?width=436&height=565',
        'https://media.discordapp.net/attachments/789206612346535936/809093070803959808/unknown-4.png?width=516&height=352',
        'https://media.discordapp.net/attachments/789206612346535936/817432589001687091/unknown.png?width=436&height=238',
        'https://media.discordapp.net/attachments/548617197287768087/748925469654515782/unknown.png?width=277&height=129',
        'https://clips.twitch.tv/UgliestSeductiveSkirretNotLikeThis-El6wylWvo6s2b6sj',
        'https://clips.twitch.tv/BlindingHonorableKiwiPartyTime-wMIeNWvwEfuyPhVu',
        'https://clips.twitch.tv/GentleHelpfulNeanderthalTF2John-MKC2Wee3qoTnppD4',
        'https://media.discordapp.net/attachments/548617197287768087/691748351078695022/unknown.png?width=272&height=82',
        'https://media.discordapp.net/attachments/767932279992483880/783118797598752798/Screenshot_20201130-205405_1.png?width=564&height=565',
        'https://media.discordapp.net/attachments/764277352162656279/822553234127323176/amigo_va_tomar_no_seu_cu.png?width=554&height=81',
        'https://media.discordapp.net/attachments/779436290835611689/823258263180542042/Screenshot_4-1.png?width=310&height=148',
        ]
    await ctx.send(f'{random.choice(momentos)}')

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


    await ctx.send(f'{"Um elitista com o anime/mangá favorito sendo", random.choice(anime), "que discute diariamente sobre", random.choice(temas), "Mas ele na verdade é um", random.choice(adjetivo), "com", random.choice(crise), "e tenta esconder através de", random.choice(metodos)}')

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
