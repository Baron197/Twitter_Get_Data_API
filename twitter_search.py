# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter API
twitter = Twitter(auth=oauth)

# tweet = twitter.search.tweets(q='#databertasbih')
# result_type = recent, popular, mixed
tweets = twitter.search.tweets(q='ridwan kamil', result_type='recent', lang='id', count=10)

print(json.dumps(tweets, indent=4))  