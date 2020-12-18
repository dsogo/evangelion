import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('', '')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#Evangelion'
numeroDeTweets = 40

for tweet in tweepy.Cursor(api.search, search).items():
    try:
        print('')
        tweet.retweet()
        tweet.favorite()
        time.sleep(45)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break