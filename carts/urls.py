from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.cart_home, name='display'),
    url(r'^update/$', views.cart_update, name='update'),
    url(r'^checkout/$', views.checkout_home, name='checkout'),
    url(r'^api/v1/change/status/$', views.change_status, name='change_status'),
    url(r'^(?P<pk>\d+)/destroy/$', views.cart_destroy, name='destroy'),
]
