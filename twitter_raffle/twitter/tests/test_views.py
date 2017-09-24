import pickle
from unittest import mock

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse

from ..models import AsyncActionReport
from .factories import AsyncActionReportFactory


class SearchViewTest(TestCase):

    @override_settings(CELERY_ALWAYS_EAGER=True)
    @mock.patch('tweepy.API.search')
    def test_post(self, mock_api_search):
        filename = settings.APPS_DIR.path('twitter', 'tests', 'fixtures',
                                          'serialize_data_q_20170910_1148.pickle').root
        with open(filename, 'rb') as input:
            tweets = pickle.load(input)

        mock_api_search.return_value = tweets
        url = reverse('twitter:search')
        response = self.client.post(url, data={'search_query': '#djangocon'})
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, AsyncActionReport.objects.count())


class AsyncActionReportListViewTest(TestCase):

    def test_get(self):
        AsyncActionReportFactory.create_batch(4, status=AsyncActionReport.OK)
        url = reverse('twitter:search-results')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '<tr>', count=5)

    def test_post(self):
        AsyncActionReportFactory.create_batch(4, status=AsyncActionReport.OK)
        AsyncActionReportFactory.create_batch(1, status=AsyncActionReport.PENDING)
        url = reverse('twitter:search-results')
        response = self.client.post(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '<tr>', count=2)
        self.assertEqual(1, AsyncActionReport.objects.count())
