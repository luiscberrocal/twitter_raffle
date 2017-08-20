from django.conf.urls import url, include
from rest_framework import routers
from twitter import views as tweet_views

router = routers.DefaultRouter()
router.register(r'tweets', tweet_views.TweetViewSet)
#urlpatterns = [url(r'^api/v1/', router.urls)]