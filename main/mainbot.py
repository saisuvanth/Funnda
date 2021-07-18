import discord
import os
import json
from discord import message
from discord import embeds
from discord.channel import TextChannel
from asyncio import sleep
from discord.activity import Game
from bs4 import BeautifulSoup as bs
from .help import cmdhelp
from .api import api
from .api import reddit_creator
import requests
from discord.ext import commands, tasks
import random
client = discord.Client()
client = commands.Bot(command_prefix=",", help_command=None)

greetings = ["Hello!:grinning:", "Hii :unamused:",
             "What Loafer :angry:", "Go to hell :expressionless:"
             "Bye! :yawning_face:", "Hello simper :imp:", "Awwww! So Sweet :smiling_face_with_3_hearts:",
             "Hello! :grin:", "Not in a mood :slight_smile:"
             ]
channels = [863786809502072842]

fcuk = ["Come on! How many times would you fuck", "Stop saying the word you can't do!", "You'll get limp dude!",
        "Aaah! Be a good child your parents want you to be", "Bad word alert!!!!!!", "Uhmm I'm gonna watch it", "Not ur job anyomore", "Daydreaming again, sweetheart?", "Baby please! Manners! You gotta ask me out for dinner first", "With what? THAT!?? Are you kidding me?",
        "No thanks. You can keep your STDs. They suit you better.", "Get in the queue.", "I don't do charity work.", "I am not that bored and you are not that lucky."]


async def on_guild_join(guild):
    ('A wild,simpy Funnda Bot hopped into the server\nBeware of this crazy bot\n')


def getjoke():
    Joke = requests.get(
        'https://v2.jokeapi.dev/joke/Any')
    joke_data = json.loads(Joke.text)
    if joke_data['type'] == 'single':
        joke = "```"+joke_data['joke']+"```"
    else:
        joke = "```"+joke_data['setup']+'\n'+joke_data['delivery']+"```"

    return joke


@client.command()
async def grant(ctx):
    await ctx.send('``` Akash tera icha pura hoga kal exam me tereko pura marks ayega par sem me fail hojayega :helpless_laugh:  ')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=Game(name='  ,help'))
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def meme(ctx):
    await ctx.send(embed=reddit_creator.subred('memes'))


@client.command()
async def subred(ctx, *, key):
    try:
        await ctx.send(embed=reddit_creator.subred(key))

    except:
        await ctx.send('Sorry! That subreddit isnt available')


@client.command()
async def pic(ctx, *, pic):
    img = api.pics(pic)
    img.set_footer(text="Information requested by: {}".format(
        ctx.author.display_name))
    await ctx.send(embed=img)


@client.command()
async def cc(ctx, *, user):
    data = api.user2(user)
    data.set_footer(text="Information requested by: {}".format(
        ctx.author.display_name))
    await ctx.send(embed=data)


@client.command()
async def cf(ctx, *, user):
    try:
        await ctx.send(embed=api.user(user))

    except:
        await ctx.send('Lmaoo that handle doesnt exist')


@client.command()
async def cfcont(ctx):
    await ctx.send(embed=api.contests())


@client.command()
async def mean(ctx, *, word):
    await ctx.send(embed=api.diction(word))


@client.command()
async def gif(ctx, *, term):
    em = api.giff(term)
    em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.message.delete()
    await ctx.send(embed=em)


@client.command()
async def anime(ctx, *, key):
    auth = 788603786452664332
    print(auth)
    if ctx.channel.is_nsfw() or ctx.message.author.id == auth:
        try:
            em = api.anime(key)
            await ctx.send(embed=em)
        except:
            await ctx.send('Cant find a anime with that :cry: ')
    else:
        await ctx.send('Approach NSFW channel horny pple')


@client.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings)+' '+f'{ctx.author.mention}')


@client.command()
async def joke(ctx):
    joke = getjoke()
    await ctx.send(joke)


@client.command()
async def mock(ctx, member: discord.Member = None):
    link = requests.get(
        'https://evilinsult.com/generate_insult.php?lang=en&amp;type=json')
    if member is None:
        await ctx.send(f'{ctx.author.mention}\n'+"```"+link.text+"```")
    else:
        await ctx.send(f'{member.mention}\n'+"```"+link.text+"```")


@client.command()
async def help(ctx, key=None):
    if key == None:
        await ctx.send(embed=cmdhelp.help())
    if key == 'cf':
        await ctx.send(embed=cmdhelp.cfhelp())
    if key == 'subred':
        await ctx.send(embed=cmdhelp.subredd())

# lists
k = {}
snipped = {}
client.editsniped_messages = {}
# events


@client.event
async def on_message_delete(message):
    if message.content.startswith(',gif'):
        return
    global k
    try:
        snipped[message.guild.id][k[message.guild.id]] = (
            message.content, message.author,        message.channel.name, message.created_at)
    except:
        snipped[message.guild.id] = {}
        k[message.guild.id] = 10
        snipped[message.guild.id][k[message.guild.id]] = (
            message.content, message.author,        message.channel.name, message.created_at)
    k[message.guild.id] = k[message.guild.id]-1
    if k[message.guild.id] == 0:
        k[message.guild.id] = 10


@client.command()
async def snipe(ctx, *, num=0):
    global k
    try:
        contents, author, channel_name, time = snipped[ctx.guild.id][k[ctx.guild.id]+num+1]
    except:
        await ctx.channel.send("No message to snipe u freak!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.purple(), timestamp=time)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)


@client.event
async def on_message_edit(message_before, message_after):
    client.editsniped_messages[message_before.guild.id] = (
        message_before.content, message_before.author, message_before.channel.name, message_after.content)


@client.command()
async def editsnipe(ctx):
    try:
        contents, author, channel_name, editedcontent = client.editsniped_messages[
            ctx.guild.id]
    except:
        await ctx.channel.send('No message to editsnipe u freak!')
        return
    embed = discord.Embed(description=contents, color=discord.Color.purple())
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Edited in : #{channel_name}")
    await ctx.channel.send(embed=embed)

perms = [788603786452664332, 384185988336844802, 759793776822059018]


@client.command()
async def redchannel(ctx, *, str):
    if ctx.author.id in perms:
        chan = ctx.channel.id
        if str == 'start':
            channels.append(chan)
            await ctx.channel.send('Channel is added to list')
        if str == 'stop':
            try:
                channels.remove(chan)
                await ctx.send('Channel deleted from list')
            except:
                await ctx.send('Channel isn\'t on list')
    else:
        await ctx.send('You cant do that')


@tasks.loop(minutes=15)
async def reddit():
    redlist = reddit_creator.looper()
    for i in channels:
        chann = client.get_channel(i)
        random_redd = random.choice(redlist)
        redd_name = random_redd.title
        redd_url = random_redd.url
        redd = discord.Embed(title=redd_name, url=redd_url)
        redd.set_image(url=redd_url)
        await chann.send(embed=redd)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif "fuck u" in message.content:
        await message.channel.send("```"+random.choice(fcuk)+"```")

    await client.process_commands(message)


@reddit.before_loop
async def before_some_task():
    await client.wait_until_ready()

reddit.start()
token = os.environ['token']
client.run(token)

