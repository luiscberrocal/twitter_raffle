from rest_framework import serializers

from .models import Tweet
from .models import TwitterUser


class TwitterUserSerializers(serializers.ModelSerializer):
    """
    Standard Serializer for TwitterUser model.
    """

    class Meta:
        model = TwitterUser
        fields = (
            'id', 'created', 'modified', 'description', 'followers_count', 'id_str', 'location', 'name', 'screen_name',
            'verified')


class TweetSerializers(serializers.ModelSerializer):
    """
    Standard Serializer for Tweet model.
    """

    class Meta:
        model = Tweet
        fields = ('id', 'created', 'modified', 'created_at', 'favorite_count', 'id_str', 'source', 'text', 'user')
