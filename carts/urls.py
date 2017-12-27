from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.cart_home, name='display'),
    url(r'^update/$', views.cart_update, name='update'),
]
