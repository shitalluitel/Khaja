from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.product_list, name='list'),
    url(r'^create/$', views.product_create, name='create'),
    # url(r'^transactions/new/$', views.transaction_create, name='transaction_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.product_edit, name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.product_delete, name='delete'),
    url(r'^(?P<pk>\d+)/$', views.product_detail, name='detail'),
    # url(r'^test/$', views.test, name='test'),
]
