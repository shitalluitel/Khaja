from django.shortcuts import render, HttpResponse
from carts.models import Quantity
from django.contrib.auth.decorators import login_required
from users.decorators import is_restaurant
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import timedelta
from django.utils import timezone

@login_required
@is_restaurant
def check_notification(request):
    company = request.user.company
    try:
        request.session['order_no'] = Quantity.objects.filter(cart__is_active= False, product__company = company).count()
        return render(request, 'company/notification.html')
    except Quantity.DoesNotExist:
        return render(request, 'company/notification.html')


@login_required
@is_restaurant
def order_list(request):
    company = request.user.company
    try:
        data = Quantity.objects.filter(cart__is_active= False, product__company = company)
    except Quantity.DoesNotExist:
        return render(request, 'company/notification.html', {'count': 0})

    if request.GET.get('per_page'):
        per_page = request.GET.get('per_page')
    else:
        per_page = 1
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'company/order_list.html', {'datas': products, 'per_page': per_page})


@login_required
@is_restaurant
def chart(request):
    return render(request, 'dashboard.html')


@login_required
@is_restaurant
def get_day_total(request):
    day_total = Quantity.objects.filter(
        timestamp__gte = (timezone.now() - timedelta(hours=20)),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
    )
    total = 0
    for data in day_total:
        total += data.product.product_price * data.quantity
    return HttpResponse("<strong><i class=\"fa fa-money \"></i> &nbsp; %s </strong> "%(total))


@login_required
@is_restaurant
def get_month_total(request):
    month_total = Quantity.objects.filter(
        timestamp__gte = (timezone.now() - timedelta(days=30)),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
    )
    total = 0
    for data in month_total:
        total += data.product.product_price * data.quantity
    return HttpResponse("<strong><i class=\"fa fa-money \"></i> &nbsp; %s </strong> "%(total))

@login_required
@is_restaurant
def get_year_total(request):
    year_total = Quantity.objects.filter(
        timestamp__gte = (timezone.now() - timedelta(days=365)),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
    )
    total = 0
    for data in year_total:
        total += data.product.product_price * data.quantity
    return HttpResponse("<strong><i class=\"fa fa-money \"></i> &nbsp; %s </strong> "%(total))


@login_required
@is_restaurant
def get_day_data(request):
    pass
