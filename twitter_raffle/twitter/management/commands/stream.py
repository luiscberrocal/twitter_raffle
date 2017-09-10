import tweepy

from ..base import TweepyCommand, MyStreamListener


class Command(TweepyCommand):
    help = 'Listen to a Twitter stream'

    def handle(self, **options):
        stream_listener = MyStreamListener(stdout=self.stdout)
        my_stream = tweepy.Stream(auth=self.api.auth, listener=stream_listener)
        my_stream.filter(track=['#djangocon'], async=True)
