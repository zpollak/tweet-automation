# This bot tweets random lines from the auy.txt text script periodically,
# using 5 second intervals.

# Housekeeping: do not edit
import tweepy
import time
from tweepy import OAuthHandler
from autotweetkeys import *
from random import randint
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
filename = open('auy.txt', 'r')
tweettext = filename.readlines()
filename.close()

# Function to select randome line from txt file
def linenum():
    return randint(0, len(tweettext))

# Function to drive twitbot
def runTime():

    line = tweettext[linenum()]
    api.update_status(line)
    print line

# Run the driver every 5 seconds
while True:
    runTime()
    print("sleeping")
    time.sleep(5)
