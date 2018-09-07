from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
from carts.models import Quantity

# Create your views here.

@login_required
def order_list(request):
    order_list = Order.objects.all().filter(user=request.user).order_by('-created_at')
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


@login_required
def order_chart_list(request,pk):
    try:
        order = Order.objects.get(order_id=pk)
        quantity = Quantity.objects.filter(cart_id = order.cart_id)
    except Quantity.DoesNotExist:
        quantity = None
    except Order.DoesNotExist:
        order = None

    context = {
        'cart' : order.cart,
        'quantity': quantity,
    }
    return render(request, 'orders/cart.html', context)
