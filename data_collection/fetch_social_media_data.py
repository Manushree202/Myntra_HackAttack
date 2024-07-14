import tweepy

# Replace with your actual bearer token
bearer_token = 'your_bearer_token_here'

# Authenticate to Twitter using the bearer token
client = tweepy.Client(bearer_token=bearer_token)

# Verify the credentials by getting user details
try:
    user = client.get_user(username='TwitterDev')
    print(f"Authenticated as: {user.data.username}")
except tweepy.TweepyException as e:
    print(f"Error: {e}")
