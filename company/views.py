from django.shortcuts import render
from carts.models import Quantity
from django.contrib.auth.decorators import login_required
from users.decorators import is_restaurant
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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

    per_page = 1
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'company/order_list.html', {'datas': products})
