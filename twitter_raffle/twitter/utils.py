import tweepy
from django.conf import settings

from twitter_raffle.twitter.management.base import TweetAdapter
from twitter_raffle.twitter.models import Tweet


class SearchTwitterUtil(object):

    def __init__(self):
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)

        self.api = tweepy.API(auth)

    def search(self, search_query):
        adapter = TweetAdapter()
        #search_query = options['search_query']
        tweets_per_qry = 100
        max_id = -1
        since_id = None
        max_tweets = 3000

        tweet_count = 0
        count = 0
        search_params = dict()
        search_params['q'] = search_query
        search_params['count'] = tweets_per_qry

        while tweet_count < max_tweets:
            if max_id <= 0:
                if since_id is not None:
                    search_params['max_id'] = str(max_id - 1)
                    search_params['since_id'] = since_id
            else:
                if since_id is None:
                    search_params['max_id'] = str(max_id - 1)
                else:
                    search_params['max_id'] = str(max_id - 1)
                    search_params['since_id'] = since_id

            new_tweets = self.api.search(**search_params)
            # serialize_data(new_tweets, format='pickle')
            if not new_tweets:
                #self.stdout.write("No more tweets found")
                break
            for tweet in new_tweets:
                tweet_data = adapter.convert(tweet)
                data = Tweet.objects.create_from_tweet_data(tweet_data)
                if data['tweet_created']:
                    #self.stdout.write('{} - {} - {}'.format(count, data['tweet'].created_at, data['tweet'].text))
                    count += 1
            tweet_count += len(new_tweets)
            max_id = new_tweets[-1].id
        return count
