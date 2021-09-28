#Author - Claysive
#Description - Just a simple test bot to practice with and try new commands. Will be working on a bit of web-scraping with this bot, so will be trying new things as I go.

#import dependencies, some may not be needed. will update as I go along
import discord
import os
import random
import requests
import praw
import eightBallRes

from discord.ext import commands
from bs4 import BeautifulSoup as bs #needed api for web-scraping

#set the prefix that will be used for commands/set the bots activity 
client = commands.Bot(command_prefix="!", activity=discord.Activity(type=discord.ActivityType.watching, name="Breaking Bad"))

#intialize the enviornment variables
token = os.environ['token']
redd_client_id = os.environ['redd_client_id']
redd_client_secret = os.environ['redd_client_secret']

#initialize the reddit api 
reddit = praw.Reddit(client_id=redd_client_id,
                     client_secret=redd_client_secret,
                     password='Python2800!',
                     user_agent="my_bot",
                     username="AllAroundBot")

#print a confirmation to the console when the bot comes online
@client.event
async def on_ready():
  print("Test Bot has come online")

#this command will allow the user to grab a random post from a subreddit of their choice. the subreddit is passed as an argurment. it then randomzies the amount of posts of that subreddit to look through  using 'randit'. currently it is set to generate a number btwn 1 and 100. prob shouldn't go higher than 100. I had some issues going higher. can be lowered though. should also update this in the future to print out an error when trying to search a subreddit that doesn't exist. currently only shows to the console. ex: !redd funny
@client.command()
async def redd(ctx, *, sub):
	post = reddit.subreddit(sub).hot()
	num_of_posts = random.randint(1, 100)
	for i in range(0, num_of_posts):
		submission = submission = next(x for x in post if not x.stickied)

	await ctx.send("Found this for you!")
	await ctx.send(submission.url)

#this command will check the users ping and print it. ex: !ping 
@client.command()
async def ping(ctx):
  await ctx.send("Ping: " + str(round(client.latency * 1000)) + "ms")

#this command will allow the user to ask a question and get a random response, simulating a magic 8 ball. ex: !8ball Will I ever become a python dev? -this pulls a random response from the 'responses' list found in eightBallRes.py
@client.command(name="8ball")
async def _8ball(ctx, *, question):
  result = random.choice(eightBallRes.responses)
  await ctx.send("Question: " + question + "\nAnswer: " + result)

#this command will be my first attempt at a "web scrape". will grab and store the html found on olympus-entertainment.com. no paramaters for this command, as all I want it to do for now is just pull the html from a static source, I may include a print function just to see how it goes. *printing did not work because the ch limit on a discord message seems to be 4000. printed this to a local file instead, which did end up working. ex: !soup
@client.command()
async def soup(ctx):
  req = requests.get('https://olympus-entertainment.com')
  soup_content = bs(req.content,'html.parser')
  fhandle = open('./soupHtml.txt','w')
  fhandle.write(str(soup_content))
  fhandle.close()
 
client.run(token) 