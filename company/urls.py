from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notification/$', views.check_notification, name='notification'),
    url(r'^order/list/$', views.order_list, name='order_list'),
]
