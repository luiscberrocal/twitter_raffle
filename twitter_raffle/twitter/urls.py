from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers


from .views import SearchView, AsyncActionReportListView, QueryPatternListView

urlpatterns = [
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^search-results/$', AsyncActionReportListView.as_view(), name='search-results'),
    url(r'^queries/$', QueryPatternListView.as_view(), name='queries'),
]
