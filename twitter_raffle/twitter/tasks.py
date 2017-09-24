from celery import shared_task

from .utils import SearchTwitterUtil

@shared_task
def fetch_and_store_tweets(search_query):
    search_util = SearchTwitterUtil()
    search_util.search(search_query)
