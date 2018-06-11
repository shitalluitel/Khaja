from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notification/$', views.check_notification, name='notification'),
    url(r'^order/list/$', views.order_list, name='order_list'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^get-day-total/$', views.get_day_total, name='day_total'),
    url(r'^get-month-total/$', views.get_month_total, name='month_total'),
    url(r'^get-year-total/$', views.get_year_total, name='year_total'),
]
