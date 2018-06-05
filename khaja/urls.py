"""khaja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from products.views import product_list
from .tasks import *

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', product_list, name="home"),
                  url(r'^users/', include('users.urls', namespace="users")),
                  url(r'^products/', include('products.urls', namespace="product")),
                  url(r'^carts/', include('carts.urls', namespace="cart")),
                  url(r'^wishlists/', include('wishlists.urls', namespace="wishlist")),
                  url(r'^address/', include('addresses.urls', namespace="address")),
                  url(r'^search/', include('search.urls', namespace="search")),
                  url(r'^customer/', include('orders.urls', namespace="order")),
                  url(r'^api/company/', include('company.urls', namespace="company")),
                  # url(r'^customer/(?P<pk>\d+)/product/list$', views.product_detail, name='detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

display.delay()
