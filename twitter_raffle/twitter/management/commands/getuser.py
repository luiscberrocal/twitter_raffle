from ..base import TweepyCommand


class Command(TweepyCommand):

    help = 'Get user info from Twitter'

    def handle(self, **options):
        user = self.api.get_user('luiscberrocal')
        print(user.screen_name)
        print(user.followers_count)
        count = 1
        for friend in user.friends():
            print('{}. {}'.format(count, friend.screen_name))
            count += 1

