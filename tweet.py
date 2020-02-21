import tweepy
import json

print("this is my twitter bot")

class twitter_bot():
    def __init__(self):
        with open("config.json") as file:
            data = json.load(file)
        self.CONSUMER_KEY = data["CONSUMER_KEY"]
        self.CONSUMER_SECRET = data["CONSUMER_SECRET"]
        self.ACCESS_KEY = data["ACCESS_KEY"]
        self.ACCESS_SECRET = data["ACCESS_SECRET"]

        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def send_tweet(self, input):
        self.api.update_status(input)