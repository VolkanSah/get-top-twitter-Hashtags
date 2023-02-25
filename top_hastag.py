import tweepy

# Set up your Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Set up the Tweepy API client
api = tweepy.API(auth)

# Retrieve the top 10 trending hashtags in your region (in this case, the USand only TOP 10 set it toyour needs)
trends = api.trends_place(23424977)[0]['trends']
hashtags = [trend['name'] for trend in trends if trend['name'].startswith('#')][:10]

# Print the top 10 trending hashtags
print('Top 10 trending hashtags on Twitter:')
for hashtag in hashtags:
    print(hashtag)
