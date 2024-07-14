import os
from dotenv import load_dotenv
import tweepy

def twitter_setup():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def collect_instagram_posts(query, count=100):
    api = twitter_setup()
    post_list = []
    
    # Use tweepy.Cursor to fetch tweets
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count):
        post_list.append(tweet.text)
    
    return post_list
