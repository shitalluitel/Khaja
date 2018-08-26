from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/order/$',views.getNewOrder, name="newOrder"),
    url(r'^prepared/order/$',views.getOrderPrepared, name="orderPrepared"),
    url(r'^cart-detail-info/$', views.deliveryCartDetail, name='cartDetail'),
    url(r'^confirm-order/$', views.confirmOrder, name="confirmOrder"),
]
