# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import OAuth, TwitterStream #, Twitter, TwitterHTTPError

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
# iterator = twitter_stream.statuses.sample()
iterator = twitter_stream.statuses.filter(track="google", language="en")

tweet_count = 10

print('[')
for tweet in iterator:
    tweet_count -= 1
    
    print(json.dumps(tweet, indent=4), ',')  
       
    if tweet_count <= 0:
        break 

print(']')
