import unittest
import json
import random
from unittest.mock import MagicMock, patch, ANY
from twitter_search import TweetFinder, OauthRequest

class TestOauthRequest(unittest.TestCase):
    pass

class TestTweetFinder(unittest.TestCase):
    def setUp(self):
        self.dummy_tweets = {'statuses':
        [{
            'user': {'screen_name': 'foobar'},
            'text': 'hello world'},
        {
            'user': {'screen_name': 'barfood'},
            'text': 'y por que no los dos?'}
        ]}

        self._make_request_original = OauthRequest.make_request

        # To avoid making requests during testing, mock the method that does so
        OauthRequest.make_request = MagicMock(
            return_value=json.dumps(self.dummy_tweets).encode('utf-8')
            )

    def tearDown(self):
        OauthRequest.make_request = self._make_request_original

    def test_init_sets_search_query(self):
        # Avoid testing methods outside of init
        with patch.object(TweetFinder, 'query_tweets'):
            finder = TweetFinder('hello')
            # Check that query_tweets() was called
            self.assertTrue(finder.query_tweets.assert_called_once())

        self.assertEqual(finder.search_query, 'hello')

    def test_query_tweets(self):
        # Test that, when TweetFinder is initialized and query_tweets() called
        # we get a list of tweets from OauthRequest
        finder = TweetFinder('hello')
        # Make sure we're calling OauthRequest
        self.assertTrue(OauthRequest.make_request.assert_called_once())
        # And check that the output is right
        self.assertListEqual(finder.tweets, self.dummy_tweets['statuses'])

    def test_get_tweet(self):
        with patch.object(random, 'randint', return_value=0):
            finder = TweetFinder('hello')
            tweet = finder.get_tweet()
            # Make sure we're actually doing this randomly
            self.assertTrue(random.randint.assert_called_once())

        # Now make sure we actually got the tweet back
        self.assertDictEqual(tweet, self.dummy_tweets['statuses'][0])
