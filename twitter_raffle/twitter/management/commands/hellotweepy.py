from ..base import TweepyCommand


class Command(TweepyCommand):

    help = 'Setup a simple tweet feed'

    def handle(self, **options):
        public_tweets = self.api.home_timeline()

        for tweet in public_tweets:
            self.stdout.write(tweet.text)










