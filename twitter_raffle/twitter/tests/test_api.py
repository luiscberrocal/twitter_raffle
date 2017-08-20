from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .factories import TweetFactory


class TestTweetViewSet(TestCase):

    def test_list(self):
        user = User.objects.get_or_create(username='lauren')[0]
        token = Token.objects.get_or_create(user=user)[0]
        TweetFactory.create_batch(5)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('api:tweets-list')
        response = client.get(url)
        self.assertEqual(5, len(response.data))





