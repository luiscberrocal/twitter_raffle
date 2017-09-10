import pickle
from unittest import mock

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase
from django_test_tools.mixins import TestCommandMixin

from twitter_raffle.twitter.models import Tweet
from ..management.base import TweepyCommand


class TestHelloTweepyCommand(TestCommandMixin, TestCase):

    @mock.patch('tweepy.API.home_timeline')
    def test_command(self, mock_home_timeline):
        filename = settings.APPS_DIR.path('twitter', 'tests', 'fixtures',
                                          'serialize_data_q_20170910_1148.pickle').root
        with open(filename, 'rb') as input:
            tweets = pickle.load(input)

        mock_home_timeline.return_value = tweets
        call_command('hellotweepy', stdout=self.content)
        results = self.get_results()
        self.assertEqual(len(results), 174)
        result = '@ericholscher I used this at #djangocon. ' \
                 'Helped to have such a concrete image to focus on, not just "don\'t be an a-hole."'
        self.assertEqual(results[0], result)


class TestSearchCommand(TestCommandMixin, TestCase):

    @mock.patch('tweepy.API.search')
    def test_command(self, mock_api_search):
        filename = settings.APPS_DIR.path('twitter', 'tests', 'fixtures',
                                          'serialize_data_q_20170910_1148.pickle').root
        with open(filename, 'rb') as input:
            tweets = pickle.load(input)

        mock_api_search.return_value = tweets
        call_command('search', stdout=self.content)
        results = self.get_results()
        self.assertEqual(len(results), 174)
        result = '1 - 2017-09-10 02:49:48 - @ericholscher I used this at #djangocon. ' \
                 'Helped to have such a concrete image to focus on, not just "don\'t be an a-hole."'
        self.assertEqual(results[0], result)
        self.assertEqual(Tweet.objects.count(), 100)
