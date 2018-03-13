from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Order


# Create your views here.


def order_list(request):
    order_list = Order.objects.all().filter(user=request.user)
    per_page = 5
    paginator = Paginator(order_list, per_page)
    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'orders/display.html', {'orders': orders})
