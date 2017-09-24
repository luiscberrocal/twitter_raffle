from django.db import models
# Create your models here.
from model_utils.models import TimeStampedModel

from .managers import TweetManager


class TwitterUser(TimeStampedModel):
    description = models.CharField(max_length=300)
    followers_count = models.IntegerField(default=0)
    id_str = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=160)
    name = models.CharField(max_length=30)
    screen_name = models.CharField(max_length=60)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class QueryPattern(TimeStampedModel):
    search_query =  models.CharField(max_length=150)

    def __str__(self):
        return self.search_query


class Tweet(TimeStampedModel):
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField(default=0)
    id_str = models.CharField(max_length=100, unique=True)
    source = models.CharField(max_length=150)
    text = models.CharField(max_length=250)
    user = models.ForeignKey(TwitterUser, related_name='tweets')

    objects = TweetManager()

class QueryPatternTweet(TimeStampedModel):
    query_pattern = models.ForeignKey(QueryPattern, related_name='tweets')
    tweet = models.ForeignKey(Tweet, related_name='query_patterns')


class AsyncActionReport(TimeStampedModel):
    PENDING = 'PENDING'
    OK = 'OK'
    FAILED = 'FAILED'

    ERROR = 'ERROR'
    INFO = 'INFO'

    MESSAGE_TYPES = (
        (ERROR, 'Error'),
        (INFO, 'Info'),
    )

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (OK, 'Ok'),
        (FAILED, 'Failed')
    )

    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=PENDING)
    message_type = models.CharField(max_length=7, choices=MESSAGE_TYPES, default=ERROR)
    message = models.TextField(null=True, blank=True)
    error_traceback = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.status
