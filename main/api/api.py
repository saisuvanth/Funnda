from datetime import date, datetime
import discord
import requests
import json
import hmtai
from bs4 import BeautifulSoup as bs
import random

anime_list = ['neko', 'ass', 'hentai', 'bdsm', 'ero', 'wallpaper',
              'manga', 'cum', 'orgy', 'blowjob', 'gangbang', 'uniform']


def contests():
    url = ' https://codeforces.com/api/contest.list?gym=false'
    url1 = 'https://codeforces.com/contests/'
    link_data = requests.get(url)
    link = json.loads(link_data.text)
    tim = str(datetime.now())
    link = link['result']
    contests = {}
    k = 0
    for i in link:
        if i['phase'] == 'BEFORE':
            ti = datetime.utcfromtimestamp(
                i['startTimeSeconds']+19800).strftime('%d-%m-%Y %H:%M:%S')
            ti = ti[:2]+'/'+ti[3:5]+'   time:'+ti[11:]
            timo = i['durationSeconds']/3600
            if timo > 24:
                Timo = str(timo/24)+' days'
            else:
                Timo = str(timo)+' hours'
            contests[k] = i['name'], ti, Timo
            k = k+1
    contests = dict([(k, v) for k, v in contests.items() if len(v) > 0])
    contests = dict(reversed(list(contests.items())))
    data = discord.Embed(title='Contests', url=url1)
    for i in contests.values():
        data.add_field(name=str(i[0]), value=i[1]+' '+str(i[2]), inline=False)
    return data


def user(user):
    url = 'https://www.codeforces.com/api/user.info?handles='+user
    link_data = requests.get(url)
    url1 = 'https://codeforces.com/profile/'+user
    link = json.loads(link_data.text)
    link = link['result'][0]
    user_img = link['avatar']
    try:
        user_rank = str(link['rating'])+','+link['rank']
        user_max = 'max : ' + str(link['maxRating'])+','+link['maxRank']
        try:
            user_place = link['organization']
            try:
                user_name = link['firstName']+' '+link['lastName']
                img = discord.Embed(title=user, url=url1)
                img.set_thumbnail(url=user_img)
                img.add_field(name=user_name,
                              value='a codeforce user', inline=False)
                img.add_field(name=user_rank, value=user_max, inline=False)
                img.add_field(name='Organisation', value=user_place)
                return img
            except:
                img = discord.Embed(title=user, url=url1)
                img.set_thumbnail(url=user_img)
                img.add_field(name=user_rank, value=user_max, inline=False)
                img.add_field(name='Organisation',
                              value=user_place, inline=False)
                return img

        except:
            img = discord.Embed(title=user, url=url1)
            img.set_thumbnail(url=user_img)
            img.add_field(name=user_rank, value=user_max, inline=False)
            return img

    except:
        img = discord.Embed(title=user, url=url1)
        img.add_field(name='Rating', value='UnRated')
        img.set_thumbnail(url=user_img)
        return img


def user2(user):
    try:
        url = 'https://www.codechef.com/users/'+user
        link_user = requests.get(url)
        info = bs(link_user.content, 'html.parser')
        user_name = info.find('h1')
        user_img = info.find('div', {'class': 'user-details-container plr10'})
        user_img = user_img.find('img')
        user_img = user_img['src']
        user_rating = info.find('div', {'class': 'rating-number'})
        user_rank = info.find('div', {'class': 'rating-ranks'})
        user_data = info.find('section', {'class': 'user-details'})
        str = user_data.find('li')
        str = str.text[10:12]
        num = []
        for i in user_rank.find_all('a'):
            num.append(i.text)
        data = discord.Embed(title=user, url=url)
        data.add_field(name=str+' '+user_name.text,
                       value='a codechef user', inline=False)
        data.add_field(name='Rating', value=user_rating.text, inline=False)
        data.add_field(name='Global Rank', value=num[0], inline=True)
        data.add_field(name='Country Rank', value=num[1], inline=True)
        data.set_thumbnail(url=user_img)
        return data
    except:
        data = discord.Embed(title='Dont stalk unknown people U IDIOT')
        return data


def diction(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word
    link = requests.get(url)
    link = json.loads(link.text)
    try:
        dic = discord.Embed(
            title=word, url='https://www.dictionary.com/browse/'+word)
        for i in link[0]['meanings']:
            dic.add_field(name=word+' as '+i['partOfSpeech'],
                          value=i['definitions'][0]['definition'], inline=False)
            try:
                dic.add_field(name='synonyms',
                              value=i['definitions'][0]['synonyms'], inline=False)
            except:
                k = 1
            try:
                dic.add_field(name='examples',
                              value=i['definitions'][0]['example'], inline=False)
            except:
                k = 1

            return dic
    except:
        dic.set_author(name='I dont know tht word :cry:')
        return dic


def anime(key):
    if key == None:
        key = random.choice(anime_list)
    try:
        pic = hmtai.useHM("v1", key)
        em = discord.Embed(title=key)
        em.set_image(url=pic)
        return em
    except:
        pic = hmtai.useHM("v2", key)
        em = discord.Embed(title=key)
        em.set_image(url=pic)
        return em


def pics(pic):
    try:
        pic.replace(" ", "+")
        url = 'https://www.google.com/search?q='+pic+'&tbm=isch&source=hp&biw=1507&bih=741&ei=Wtq1YJ7cKuWO4-EPtr666AM&oq='+pic + \
            '&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzICCAAyBQgAELEDMgUIABCxAzIFCAAQsQM6CAgAELEDEIMBUPEMWMITYNgUaAFwAHgAgAG3AogB1gSSAQUyLTEuMZgBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img&ved=0ahUKEwie8cnY7fXwAhVlxzgGHTafDj0Q4dUDCAc&uact=5'
        link = requests.get(url)
        soup = bs(link.content, 'html.parser')
        images = []
        for item in soup.find_all('img', limit=10):
            images.append(item['src'])
        images = images[1:]
        image = random.choice(images)
        img = discord.Embed(title=pic)
        img.set_image(url=image)
        return img
    except:
        data = discord.Embed(title='My knowledge is aint greater that great')
        return data


def giff(term):
    key = 'SEKXVN8NC273'
    url = 'https://g.tenor.com/v1/search?q=%s&key=%s&limit=3&media_filter=minimal' % (
        term, key)
    link = requests.get(url)
    link = json.loads(link.content)
    gifs = []
    for i in link['results']:
        gifs.append(i['media'][0]['gif']['url'])
    em = discord.Embed(title='')
    em.set_image(url=random.choice(gifs))
    return em
