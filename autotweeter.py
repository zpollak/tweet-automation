# This bot tweets random lines from the auy.txt text script periodically,
# using 5 second intervals.

# Load required packages
import tweepy
import time
from autotweetkeys import *
from random import randint

# Link Twitter API and load Consumer and Access key/secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
filename = open('auy.txt', 'r')
tweettext = filename.readlines()
filename.close()

# Function to select randome line from txt file
def line_num():
    return randint(0, len(tweettext))

# Update status with random line from `auy.txt` every .5 seconds
# Timestamps are included because Twitter blocks duplicate tweets
for line in tweettext:
    tm = time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')
    line = tweettext[line_num]
    tweetout = line + tm
    api.update_status(tweetout)
    print tweetout
    print '...'
    time.sleep(.5)
# The bot has tweeted the entire file
print "All done!"
