from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notification/$', views.check_notification, name='notification'),
    url(r'^order/list/$', views.order_new_list, name='order_new_list'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^get-day-total/$', views.get_day_total, name='day_total'),
    url(r'^get-month-total/$', views.get_month_total, name='month_total'),
    url(r'^get-year-total/$', views.get_year_total, name='year_total'),
    url(r'^get-day-data/$', views.get_day_data, name='get_day_data'),
    url(r'^count-product/$', views.total_product, name="count_product"),
    url(r'^product/list$', views.company_product_list, name="product_list"),
    url(r'^edit$', views.company_edit, name="edit"),
]
