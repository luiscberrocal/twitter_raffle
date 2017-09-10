from django_test_tools.file_utils import serialize_data

from ...models import Tweet
from ..base import TweepyCommand, TweetAdapter


class Command(TweepyCommand):
    help = 'search Twitter stream'

    def add_arguments(self, parser):
        parser.add_argument('search_query')
        # parser.add_argument("-l", "--list",
        #                     action='store_true',
        #                     dest="list",
        #                     help="List employees",
        #                     )
        # parser.add_argument("-a", "--assign",
        #                     action='store_true',
        #                     dest="assign",
        #                     help="Create unit assignments",
        #                     )
        #
        # parser.add_argument("--office",
        #                     dest="office",
        #                     help="Organizational unit short name",
        #                     default=None,
        #                     )
        # parser.add_argument("--start-date",
        #                     dest="start_date",
        #                     help="Start date for the assignment",
        #                     default=None,
        #                     )
        # parser.add_argument("--fiscal-year",
        #                     dest="fiscal_year",
        #                     help="Fiscal year for assignments",
        #                     default=None,
        #                     )
        # parser.add_argument("-u", "--username",
        #                 dest="usernames",
        #                 help="LDAP usernames for employees",
        #                 nargs='+',
        #                 )

    def handle(self, **options):
        adapter = TweetAdapter()
        search_query = options['search_query']
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
            #serialize_data(new_tweets, format='pickle')
            if not new_tweets:
                self.stdout.write("No more tweets found")
                break
            for tweet in new_tweets:
                tweet_data = adapter.convert(tweet)
                data = Tweet.objects.create_from_tweet_data(tweet_data)
                if data['tweet_created']:
                    self.stdout.write('{} - {} - {}'.format(count, data['tweet'].created_at, data['tweet'].text))
                    count += 1
            tweet_count += len(new_tweets)
            max_id = new_tweets[-1].id
