from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.product_list, name='list'),
    url(r'^create/$', views.product_create, name='create'),
    # url(r'^transactions/new/$', views.transaction_create, name='transaction_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.product_edit, name='edit'),
    # url(r'^transactions/(?P<pk>\d+)/delete/$', views.transaction_delete, name='transaction_delete'),
    # url(r'^transactions/(?P<pk>\d+)/paid/$', views.transaction_cash_paid, name='transaction_cash_paid'),
]
