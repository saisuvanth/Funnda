import discord
from discord.ext.commands.converter import ColorConverter


def help():
    elpin = discord.Embed(
        title='help', ColorConverter=discord.colour.Color.blue)
    elpin.add_field(name=',hello', value='to greet me :smile: ', inline=True)
    elpin.add_field(name=',joke', value='want a joke :laughing: ', inline=True)
    elpin.add_field(
        name=',mock', value='to mock a specified user :stuck_out_tongue_closed_eyes: ', inline=True)
    elpin.add_field(name=',meme', value='to get a meme :robot: ', inline=True)
    elpin.add_field(name=',cc', value='for user info <username>', inline=True)
    elpin.add_field(
        name=',pic', value='give anything to get its picture :camera_with_flash: ', inline=True)
    elpin.add_field(name=',wiki', value='for info on smthng', inline=True)
    elpin.add_field(name=',cf', value='for help ```,help cf```', inline=True)
    elpin.add_field(
        name=',subred', value='for help ```,help subred```', inline=True)
    return elpin


def cfhelp():
    elpin = discord.Embed(
        title='cf help', ColorConverter=discord.colour.Color.blue)
    elpin.add_field(name='For CF user info',
                    value='```,cf <handle>```', inline=False)
    elpin.add_field(name='For contests', value='```,cfcont```', inline=False)
    return elpin


def subredd():
    url = 'https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits/'
    elpin = discord.Embed(title='subreddits', url=url)
    elpin.add_field(name='anime or comics',
                    value='comics,marvel,defenders,pokemon,naruto,ShingekiNoKyojin,anime,manga,etc')
    elpin.add_field(name='tech and Science',
                    value='Science,gamedev,ubuntu,coding,learnprogramming,java,cpp,howtohack,YouShouldKnow,etc')
    elpin.add_field(
        name='Fun', value='Jokes,dankmemes,MemeEconomy,funny,movies,Cringetopia,Twitch,WTF,facepalm')
    elpin.add_field(
        name='NSFW', value='toosoon,roastme,imgoingtohellforthis,darkmeme,DarkJoke,dark_humour,etc')
    elpin.add_field(name='U can use any subreddit u want',
                    value='please see nsfw in NSFW channel :slight_smile: ')
    return elpin


def anime():
    s = '```'
    str = s+'neko'+s+s+'ass'+s+s+'bdsm'+s+s+'cum'+s+s+'manga'+s+s+'hentai'+s+s+'orgy' + \
        s+s+'cuckold'+s+s+'blowjob'+s+s+'gangbang' + \
            s+s+'wallpaper'+s+s+'ero'+s+s+'uniform'+s
    em = discord.Embed(title='anime help')
    em.add_field(name='commands', value=str, inline=True)
    return em
