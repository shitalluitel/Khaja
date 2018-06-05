from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def order_list(request):
    order_list = Order.objects.all().filter(user=request.user).order_by('created_at')
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
