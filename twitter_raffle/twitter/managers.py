from django.db import models


class TweetManager(models.Manager):
    def create_from_tweet_data(self, tweet_data):
        from .models import TwitterUser
        user_created = False
        tweet_created = False
        tweet = None
        try:
            user = TwitterUser.objects.get(id_str=tweet_data['user']['id_str'])
        except TwitterUser.DoesNotExist:
            user = TwitterUser.objects.create(**tweet_data['user'])
            user_created = True
        try:
            tweet = self.get(id_str=tweet_data['tweet']['id_str'])
        except self.model.DoesNotExist:
            tweet_data['tweet']['user'] = user
            tweet = self.create(**tweet_data['tweet'])
            tweet_created = True
        return {'tweet': tweet, 'tweet_created': tweet_created, 'user_created': user_created}
