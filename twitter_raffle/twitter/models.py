from django.db import models
# Create your models here.
from model_utils.models import TimeStampedModel

from .managers import TweetManager


class TwitterUser(TimeStampedModel):
    description = models.CharField(max_length=300)
    followers_count = models.IntegerField(default=0)
    id_str = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=150)
    name = models.CharField(max_length=30)
    screen_name = models.CharField(max_length=60)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tweet(TimeStampedModel):
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField(default=0)
    id_str = models.CharField(max_length=100, unique=True)
    source = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    user = models.ForeignKey(TwitterUser, related_name='tweets')

    objects = TweetManager()
