from django.contrib import admin

# Register your models here.
from .models import Tweet, TwitterUser, AsyncActionReport, QueryPattern


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'created')


@admin.register(TwitterUser)
class TwitterUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'screen_name', 'location', 'created')

@admin.register(AsyncActionReport)
class AsyncActionReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'message_type', 'message', 'created', 'modified')


@admin.register(QueryPattern)
class QueryPatternAdmin(admin.ModelAdmin):
    list_display = ('search_query',)
