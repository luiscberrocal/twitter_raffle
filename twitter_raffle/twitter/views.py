# Create your views here.
from django import forms, views
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from rest_framework import viewsets, filters

from twitter_raffle.twitter.tasks import fetch_and_store_tweets, fetch_data_and_store_it
from .forms import SearchForm
from .models import Tweet, AsyncActionReport, QueryPattern
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
        form = self.get_form()
        if form.is_valid():
            query = form.cleaned_data['search_query']
            async_result = fetch_data_and_store_it.delay(query)
            msg = 'Task {} running for query {}'.format(async_result.task_id, query)
            messages.add_message(self.request, messages.SUCCESS, msg)

        return super(SearchView, self).post(request, *args, **kwargs)

class QueryPatternListView(ListView):
    model = QueryPattern
    context_object_name = 'query_patterns'
    template_name = 'twitter/query-patterns.html'


class AsyncActionReportListView(ListView):
    model = AsyncActionReport
    context_object_name = 'async_reports'
    template_name = 'twitter/search_results.html'
    ordering = ('-created',)

    def post(self, request, *args, **kwargs):
        AsyncActionReport.objects.filter(status=AsyncActionReport.OK).delete()
        return self.get(request, *args, **kwargs)


