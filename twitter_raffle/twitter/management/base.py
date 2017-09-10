import logging

import tweepy
from django.conf import settings
from django.core.management import BaseCommand

from ..models import TwitterUser, Tweet

logger = logging.getLogger(__name__)


class TweepyCommand(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)

        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)

        self.api = tweepy.API(auth)
        logger.debug('{} : {}'.format('settings.TWITTER_CONSUMER_KEY', settings.TWITTER_CONSUMER_KEY))
        logger.debug('{} : {}'.format('settings.TWITTER_CONSUMER_SECRET', settings.TWITTER_CONSUMER_SECRET))
        logger.debug('{} : {}'.format('settings.TWITTER_ACCESS_TOKEN', settings.TWITTER_ACCESS_TOKEN))
        logger.debug('{} : {}'.format('settings.TWITTER_TOKEN_SECRET', settings.TWITTER_TOKEN_SECRET))

        super(TweepyCommand, self).__init__(stdout, stderr, no_color)


class TweetAdapter(object):
    def convert(self, tweet):
        tweet_data = dict()
        tweet_data['tweet'] = dict()
        tweet_data['tweet']['created_at'] = tweet.created_at
        tweet_data['tweet']['favorite_count'] = tweet.favorite_count
        tweet_data['tweet']['id_str'] = tweet.id_str
        tweet_data['tweet']['source'] = tweet.source
        tweet_data['tweet']['text'] = tweet.text

        tweet_data['user'] = dict()
        if tweet.user.description is None:
            tweet_data['user']['description'] = 'UNKNOWN'
        else:
            tweet_data['user']['description'] = tweet.user.description
        tweet_data['user']['followers_count'] = tweet.user.followers_count
        tweet_data['user']['id_str'] = tweet.user.id_str
        if tweet.user.location is None:
            tweet_data['user']['location'] = 'UNKNOWN'
        else:
            tweet_data['user']['location'] = tweet.user.location
        tweet_data['user']['name'] = tweet.user.name
        tweet_data['user']['screen_name'] = tweet.user.screen_name
        tweet_data['user']['verified'] = tweet.user.verified
        return tweet_data


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None, **kwargs):
        super().__init__(api)
        self.stdout = kwargs.get('stdout')
        self.adapter = TweetAdapter()

    def on_status(self, status):
        tweet_data = self.adapter.convert(status)
        user, created = TwitterUser.objects.get_or_create(**tweet_data['user'])
        tweet_data['tweet']['user'] = user
        Tweet.objects.get_or_create(**tweet_data['tweet'])

        if self.stdout is not None:
            self.stdout.write(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False
