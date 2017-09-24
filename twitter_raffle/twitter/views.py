# Create your views here.
from django import forms, views
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import viewsets, filters

from twitter_raffle.twitter.tasks import fetch_and_store_tweets, fetch_data_and_store_it
from .forms import SearchForm
from .models import Tweet
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_friends = ('user_name',)


class SearchView(FormView):
    template_name = 'twitter/search.html'
    form_class = SearchForm
    success_url = reverse_lazy('twitter:search-results')

    def post(self, request, *args, **kwargs):
        async_result = fetch_data_and_store_it('#djangocon')
        messages.add_message(self.request, messages.SUCCESS, 'Running task {}'.format(async_result.task_id))

        return super(SearchView, self).post(request, *args, **kwargs)
