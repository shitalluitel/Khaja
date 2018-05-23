from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.create, name='create'),
    url(r'^$', views.list, name='list'),
]
