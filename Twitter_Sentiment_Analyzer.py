import tweepy
from textBlob import textblob

consumer_key = 3YLzOQPjPyQ6lVzOxj83ynL6S
consumer_secret = aH3f2aR5jG8QPU4nGzsKYhbUpvJhRjrQZWkXiA9YDtnTaDSwBX

access_token =  969640262543687680-R4Vkox0E0TuMj1BqwpqjFCogRLDO7gV
access_token_secret = 18ulGTtFYgaWNCCsdtTgV7JOypTMyao53V9IJXq1dQtJT

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = auth.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.Sentiment)