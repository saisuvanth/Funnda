import discord
import praw
import random


reddit = praw.Reddit(client_id="KMRD--nImElMww",
                     client_secret="oXc9xxg7WPO7feODenqJQhchkFv1LA",
                     username="whitedevil069",
                     password="suvanth@96",
                     user_agent="fundaa"
                     )

subreddits = ['meme', 'ProgrammingHumour', '4chan',
              'dankmemes', 'ComedyCemetery', 'MemeEconomy']


def subred(type):
    submissions = reddit.subreddit(type)
    top = submissions.hot(limit=25)
    redd_list = []
    for subredds in top:
        redd_list.append(subredds)

    random_redd = random.choice(redd_list)
    redd_name = random_redd.title
    redd_url = random_redd.url
    redd = discord.Embed(title=redd_name)
    redd.set_image(url=redd_url)
    return redd


def looper():
    type = random.choice(subreddits)
    submissions = reddit.subreddit(type)
    top = submissions.hot(limit=25)
    redd_list = []
    for subredds in top:
        redd_list.append(subredds)
    return redd_list
