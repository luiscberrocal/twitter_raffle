# Create your views here.
from rest_framework import viewsets, filters

from .models import Tweet
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_friends = ('user_name',)
