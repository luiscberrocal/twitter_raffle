import tweepy

from twitter_raffle.twitter.models import Tweet
from ..base import TweepyCommand, MyStreamListener, TweetAdapter



class Command(TweepyCommand):

    help = 'search Twitter stream'

    def handle(self, **options):
        adapter = TweetAdapter()
        search_query = '#djangocon'
        tweets_per_qry = 100
        max_id = -1
        since_id = None
        max_tweets = 2000

        tweet_count = 0
        count = 1
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
            if not new_tweets:
                self.stdout.write("No more tweets found")
                break
            for tweet in new_tweets:
                tweet_data = adapter.convert(tweet)
                data = Tweet.objects.create_from_tweet_data(tweet_data)
                if data['tweet_created']:
                    self.stdout.write('{} - {} - {}'.format(count, data['tweet'].created_at,  data['tweet'].text))
                    count += 1
            tweet_count += len(new_tweets)
            max_id = new_tweets[-1].id


