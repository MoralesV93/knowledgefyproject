import tweepy
import json
from tweepy import OAuthHandler
 
consumer_key = '1vsbPxMS7rPFygwfu7fmwhiL2'
consumer_secret = 'VRDpSoma3PvraNY9eDRjJrUIkMHaIx5HN6zmT5QCCs7TctEEo4'
access_token = '1123524671956234240-upXtRVU5S2nL9KMLAjcEAJWf4LwhsX'
access_secret = '9bU6oCuIiQbJBKfyDtM8E8zAVbpsVv8v0jkFmeN18ES6i'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#print(user)
def process_or_store(tweet):
    print(json.dumps(tweet))

for tweet in api.user_timeline(15037438):
    process_or_store(tweet._json)

'''
try:
    tweet = api.get_status('ByronUnir')
    print('get_tweets_single: fetching tweet for ID %s', tweet_id)
except tweepy.TweepError as te:
    print('get_tweets_single: failed to get tweet ID %s: %s', 15037438, te.message)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
    '''