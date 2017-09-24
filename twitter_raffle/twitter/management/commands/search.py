from twitter_raffle.twitter.utils import SearchTwitterUtil
from ..base import TweepyCommand, TweetAdapter
from ...models import Tweet


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
        tweet_util = SearchTwitterUtil(stdout=self.stdout)
        search_query = options['search_query']
        tweet_util.search(search_query)
