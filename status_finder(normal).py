import tweepy
consumer_key = "YOUR CONSUMER KEY"
consumer_secret = "YOUR CONSUMER SECRET"
access_token = "YOUR ACCESS TOKEN"
access_token_secret = "YOUR ACCESS SECRET"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
control = tweepy.API(auth)
target = int(str(input("TWEET ID ")))
status = control.get_status(target)
print(str(status))
