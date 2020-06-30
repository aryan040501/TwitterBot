import tweepy

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)
user = api.me()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print("\n")
print(user.name)
print("\n")
print(user.followers_count)