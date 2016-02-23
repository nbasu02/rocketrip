from urllib.parse import urlencode
import oauth2
import json
import random
import os

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_KEY_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

def oauth_req(url, http_method="GET", post_body='', http_headers=None):
    '''
    Makes request to twitter.  Snippet found from twitter's documentation:
    https://dev.twitter.com/oauth/overview/single-user
    '''
    consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
    token = oauth2.Token(key=access_token, secret=access_token_secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url.encode('utf-8'), method=http_method, body=post_body.encode('utf-8'), headers=http_headers )
    return content

results = oauth_req('https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi')

class TweetFinder(object):
    '''
    Given a search string, stores tweets matching the query.  Can also
    return a random tweet from the stored tweets.
    '''

    BASE_URL = 'https://api.twitter.com/1.1/search/tweets.json?'

    def __init__(self, search_query):
        '''
        search_query is any string that can be used to search twitter.  See:
        https://dev.twitter.com/rest/public/search
        for details
        '''
        self.search_query = search_query
        self.query_tweets()

    def query_tweets(self):
        '''
        Searches for tweets and stores
        '''
        url = self.BASE_URL + urlencode({'q': self.search_query})
        results = oauth_req(url)
        results = json.loads(results.decode('utf-8'))
        self.tweets = results['statuses']

    def get_tweet(self):
        '''
        Randomly returns the text of one tweet from this object's stored tweets
        '''
        index = random.randint(0, len(self.tweets)-1)
        return self.tweets[index]['text']

finder = TweetFinder('hello world')
for i in range(3):
    print(finder.get_tweet())
