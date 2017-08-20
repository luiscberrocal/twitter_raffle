from django.test import TestCase

from twitter_raffle.twitter.models import Tweet
from ..management.base import TweetAdapter
from .factories import MockTweetFactory


class TweetTest(TestCase):

    def test_create_from_tweet_data(self):
        twitter_tweet = MockTweetFactory.create()
        adapter = TweetAdapter()
        tweet_data = adapter.convert(twitter_tweet)
        data = Tweet.objects.create_from_tweet_data(tweet_data)
        self.assertEqual(1, Tweet.objects.count())
        self.assertIsNotNone(data['tweet'].pk)
        self.assertTrue(data['tweet_created'])
        self.assertTrue(data['user_created'])
