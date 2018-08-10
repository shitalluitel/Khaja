from django.conf.urls import url

from .views import SearchProductView, search_option

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name="query"),
    url(r'^api/find/product$', search_option, name="search_option"),
]
