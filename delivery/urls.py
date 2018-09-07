from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/order/$',views.getNewOrder, name="newOrderAPI"),
    url(r'^prepared/order/$',views.getOrderPrepared, name="orderPreparedAPI"),
    url(r'^cart-detail-info/$', views.deliveryCartDetail, name='cartDetail'),
    url(r'^confirm-order/$', views.confirmOrder, name="confirmOrder"),
    url(r'^order/new/$', views.newDeliveryOrder, name="newOrder"),
    url(r'^order/prepared/$', views.preparedDeliveryOrder, name="preparedOrder"),
    url(r'^order/paid/$', views.paidOrder, name="paidOrder"),
    url(r'^order/paid-list/$', views.paidOrderList, name="paidOrderList"),
    url(r'^notification/$', views.checkDeliveryNotification, name="checkDeliveryNotification"),
    url(r'^paid/cart-detail-info/$', views.deliveryPaidCartDetail, name="deliveryPaidCartDetail"),
    url(r'^delete/order/(?P<cart_id>\w+)/$', views.deleteOrder, name="deleteOrder"),
]
