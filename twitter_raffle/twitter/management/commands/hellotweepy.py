import logging

from ..base import TweepyCommand

logger = logging.getLogger(__name__)


class Command(TweepyCommand):
    help = 'Setup a simple tweet feed'

    def handle(self, **options):
        public_tweets = self.api.home_timeline()
        count = 1
        for tweet in public_tweets:
            logger.debug('{} - {}'.format(count, tweet.text))
            self.stdout.write(tweet.text)
            count += 1
