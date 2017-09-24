from django.db import models



class TweetManager(models.Manager):
    def create_from_tweet_data(self, tweet_data):
        from .models import TwitterUser, QueryPattern, QueryPatternTweet
        user_created = False
        tweet_created = False
        tweet = None
        query_pattern = QueryPattern.objects.get_or_create(search_query=tweet_data['search_query'])[0]
        try:
            user = TwitterUser.objects.get(id_str=tweet_data['user']['id_str'])
        except TwitterUser.DoesNotExist:
            user = TwitterUser.objects.create(**tweet_data['user'])
            user_created = True
        try:
            tweet = self.get(id_str=tweet_data['tweet']['id_str'])
            QueryPatternTweet.objects.get_or_create(
                query_pattern=query_pattern,
                tweet=tweet
            )
        except self.model.DoesNotExist:
            tweet_data['tweet']['user'] = user
            tweet = self.create(**tweet_data['tweet'])
            tweet_created = True
        return {'tweet': tweet, 'tweet_created': tweet_created, 'user_created': user_created}
