class Tweet:
    
    def __init__(self, tweetObject):
        self.text = tweetObject['text']
        self.hashtags = tweetObject['entities']['hashtags']
        if 'retweeted_status' in tweetObject:
            self.ownerTweetId = tweetObject['retweeted_status']['user']['id']
            self.ownerTweetDescription =  tweetObject['retweeted_status']['user']['description']
            self.ownerTweetFollowing = tweetObject['retweeted_status']['user']['following']
            self.tweetType = 'retweet'
        elif 'quoted_status' in tweetObject :
            self.ownerTweetId = tweetObject['quoted_status']['user']['id']
            self.ownerTweetDescription =  tweetObject['quoted_status']['user']['description']
            self.ownerTweetFollowing = tweetObject['quoted_status']['user']['following']
            self.tweetType = 'sharedtweet'
        else:
            self.ownerTweetId = tweetObject['user']['id']
            self.ownerTweetDescription =  tweetObject['user']['description']
            self.ownerTweetFollowing = False
            self.tweetType = 'tweet'