import tweepy
import json
import sys
from tweepy import OAuthHandler
from model.tweet import Tweet
from model.pfwords import Word
from model.score import Score
from collections import namedtuple

consumer_key = '1vsbPxMS7rPFygwfu7fmwhiL2'
consumer_secret = 'VRDpSoma3PvraNY9eDRjJrUIkMHaIx5HN6zmT5QCCs7TctEEo4'
access_token = '1123524671956234240-upXtRVU5S2nL9KMLAjcEAJWf4LwhsX'
access_secret = '9bU6oCuIiQbJBKfyDtM8E8zAVbpsVv8v0jkFmeN18ES6i'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = []

professionalwordArray = []
knowloadgewordArray = []

matchWordScore = []


# print(user)
def process_or_store(tweet):
    print(json.dumps(tweet, indent=4))


def readProfessionalWords():
    with open('data/professionalwords.json') as f:
        professionalwords = json.load(f)
    for word in professionalwords:
        _word = Words(word)
        professionalwordArray.append(_word)


def readKnowloadgeWords():
    with open('data/knowloadge.json') as f:
        knowloadewords = json.load(f)
    for word in knowloadewords:
        _word = Words(word)
        knowloadgewordArray.append(_word)


def matchWordTweet(_word: Word, _tweet: Tweet):
    matched = False
    if(_word.)

def formatText():


for tweet in api.user_timeline(1123524671956234240):
    p = tweet._json
    # print(json.loads(json.dumps(p))['retweeted_status'])
    tweets.append(json.loads(json.dumps(p)))
    test = Tweet(json.loads(json.dumps(p)))
    # print(test)
process_or_store(tweets)
