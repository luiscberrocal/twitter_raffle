from django.contrib import admin

# Register your models here.
from .models import Tweet, TwitterUser


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


@admin.register(TwitterUser)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('name', 'screen_name')
