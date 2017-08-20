from datetime import datetime
from unittest.mock import Mock

from django.test import TestCase

from twitter.management.base import TweetAdapter


class TweetAdapterTest(TestCase):

    def test_convert(self):

        mock_tweet = Mock()
        mock_tweet.created_at = datetime(2017, 1, 1, 13, 15)
        mock_tweet.favorite_count = 2
        mock_tweet.id_str = '123424254422'
        mock_tweet.source = 'Kilo'
        mock_tweet.text = 'Lucky tweet #djangocon'
        mock_tweet.user = Mock()
        mock_tweet.user.description = 'Thundergod'
        mock_tweet.user.followers_count = 2
        mock_tweet.user.id_str = '2123'
        mock_tweet.user.location = 'Pty'
        mock_tweet.user.name = 'Thundergod'
        mock_tweet.user.screen_name = 'Thor'
        mock_tweet.user.verified = False

        adapter = TweetAdapter()
        tweet_data = adapter.convert(mock_tweet)
        self.assertEqual(mock_tweet.created_at, tweet_data['created_at'])
        self.assertEqual(mock_tweet.favorite_count, tweet_data['favorite_count'])
        self.assertEqual(mock_tweet.id_str, tweet_data['id_str'])
        self.assertEqual(mock_tweet.source, tweet_data['source'])
        self.assertEqual(mock_tweet.text, tweet_data['text'])
        self.assertEqual(mock_tweet.user.description, tweet_data['user_description'])

