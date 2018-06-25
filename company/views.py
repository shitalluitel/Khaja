from django.shortcuts import render, HttpResponse
from carts.models import Quantity
from django.contrib.auth.decorators import login_required
from users.decorators import is_restaurant
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import timedelta
from django.utils import timezone
from products.models import Product
import json
from .models  import Company

status_list = ["New","Received","Preparing","Cooked","Delivered","Canceled"]

@login_required
@is_restaurant
def check_notification(request):
    company = request.user.company
    try:
        request.session['order_no'] = Quantity.objects.filter(cart__is_active= False, product__company = company, status="New").count()
        return render(request, 'company/notification.html')
    except Quantity.DoesNotExist:
        return render(request, 'company/notification.html')

def company_product_list(request):
    company_id = request.GET.get("company")
    company_name = Company.objects.get(company_id= company_id)
    try:
        product_list_data = Product.objects.filter(company= company_name)
    except Product.DoesNotExist:
        return redirect("product:list")

    per_page = 8
    paginator = Paginator(product_list_data, per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'company/company_product_list.html', {'products': products, 'company':company_name})

@login_required
@is_restaurant
def order_new_list(request):
    status = request.GET.get("status")
    products, per_page = order_list_query(request=request, status=status)
    return render(request, 'company/order_list.html', {'datas': products, 'per_page': per_page})

@login_required
@is_restaurant
def order_list_query(request, status):
    company = request.user.company
    if status not in status_list:
        status= "New"
    try:
        data = Quantity.objects.filter(cart__is_active= False, product__company = company, status =status ).order_by("-timestamp")
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

    return products, per_page

@login_required
@is_restaurant
def chart(request):
    request.session['order_no'] = Quantity.objects.filter(cart__is_active= False, product__company = request.user.company, status="New").count()
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
def total_product(request):
    return HttpResponse("<strong> %s</strong>" % (Product.objects.filter(company = request.user.company).count()))


@login_required
@is_restaurant
def get_day_data(request):
    start_time = (timezone.now() - timedelta(hours=24))
    end_time = timezone.now()
    datas = Quantity.objects.filter(
        timestamp__range = (start_time, end_time),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
        )

    labels = []
    return_data = [] # data that gets returned

    for i in range(0,24):
        total = 0
        new_data = datas.filter(timestamp__range =(start_time + timedelta(hours = i), start_time + timedelta(hours=(i+1)) ))
        for data in new_data:
            total += data.product.product_price * data.quantity
        if total > 0:
            return_data.append(str(total))
            labels.append("%s"%((timezone.now() - timedelta(hours = 24 -i)).strftime("%I %p")))

    response_data = {}
    response_data['labels'] = labels
    response_data['data'] = return_data
    response_data['label'] = "Transaction within 24 hrs"
    return HttpResponse(json.dumps(response_data), content_type="application/json")
