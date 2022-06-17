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

# Get a particular user's timeline (up to 3,200 of his/her most recent tweets)
tweets = twitter.statuses.user_timeline(screen_name="MistrRaiz_22")

print(json.dumps(tweets, indent=4))  