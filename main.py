#import dependencies
import discord
import os
import random
import requests
import json
import praw
import eightBallRes


from discord.ext import commands

#set the prefix that will be used for commands/set the bots activity 
client = commands.Bot(command_prefix="!", activity=discord.Activity(type=discord.ActivityType.watching, name="Breaking Bad"))

#intialize the enviornment variables
token = os.environ['token']
redd_client_id = os.environ['redd_client_id']
redd_client_secret = os.environ['redd_client_secret']

#intalize the reddit api 
reddit = praw.Reddit(client_id=redd_client_id,
                     client_secret=redd_client_secret,
                     password='Python2800!',
                     user_agent="my_bot",
                     username="AllAroundBot")

#print a confirmation to the console when the bot comes online
@client.event
async def on_ready():
  print("Test Bot has come online")

#this command will allow the user to grab a random post from a subreddit of their choice. the subreddit is passed as an argurment. ex: !redd funny
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

#this command will allow the user to ask a question and get a random response, simulating a magic 8 ball. ex: !8ball Will I ever become a python dev?
@client.command(name="8ball")
async def _8ball(ctx, *, question):
  result = random.choice(eightBallRes.responses)
  await ctx.send("Question: " + question + "\nAnswer: " + result)

client.run(token) 