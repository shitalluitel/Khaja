from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^order$', views.order_list, name='list'),
    url(r'^order/(?P<pk>\w+)/cart/$', views.order_chart_list, name='chart_list'),
]
