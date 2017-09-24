from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers


from .views import SearchView



urlpatterns = [
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^search-results/$', TemplateView.as_view(template_name='twitter/search_results.html'), name='search-results'),
]
