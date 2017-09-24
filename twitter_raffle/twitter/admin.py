from django.contrib import admin

# Register your models here.
from .models import Tweet, TwitterUser, AsyncActionReport


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


@admin.register(TwitterUser)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('name', 'screen_name')

@admin.register(AsyncActionReport)
class AsyncActionReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'message_type', 'message')
