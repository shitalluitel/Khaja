from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.decorators import is_delivery
from orders.models import Order
from carts.models import Cart, Quantity
from addresses.models import Address
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.http import JsonResponse
# Create your views here.



@login_required
@is_delivery
def deliveryDashboard(request):
    return render(request, 'delivery/dashboard.html')


@login_required
@is_delivery
def getNewOrder(request):
    orderData = Order.objects.filter(status="Recieved", cart__is_active = True).order_by('-created_at')[:5]

    return render(request, 'delivery/deliveryTable.html', {'order': orderData})


@login_required
@is_delivery
def getOrderPrepared(request):
    orderData = Order.objects.filter(status="Prepared", cart__is_active = False)[:5]
    return render(request, 'delivery/deliveryTable.html', {'order': orderData})


@login_required
@is_delivery
def deliveryCartDetail(request):
    cart_id = request.GET.get('cart_id')

    cartData = Cart.objects.get(cart_id= cart_id)
    quantityData = Quantity.objects.filter(cart= cartData)
    try:
        addressData = Address.objects.get(cart__cart_id= cart_id)
    except Address.DoesNotExist:
        addressData = None
    print(addressData)
    context = {
        'cart': cartData,
        'quantity': quantityData,
        'address': addressData,
    }

    return render(request, 'delivery/deliveryCartInfo.html', context=context)


@login_required
@is_delivery
def deliveryPaidCartDetail(request):
    cart_id = request.GET.get('cart_id')

    cartData = Cart.objects.get(cart_id= cart_id)
    quantityData = Quantity.objects.filter(cart= cartData).order_by('-created_at')
    try:
        addressData = Address.objects.get(cart__cart_id= cart_id)
    except Address.DoesNotExist:
        addressData = None
    print(addressData)
    context = {
        'cart': cartData,
        'quantity': quantityData,
        'address': addressData,
    }

    return render(request, 'delivery/deliveryPaidCartInfo.html', context=context)

@login_required
@is_delivery
def confirmOrder(request):
    cart_id = request.GET.get("cart_id")

    cart = Cart.objects.get(cart_id = cart_id)

    order_id = request.GET.get('order_id')
    order = Order.objects.get(cart__cart_id = cart_id)

    order.status = "Processing"
    order.save()

    cart.is_active = False
    cart.save()
    # return HttpResponse("Comfirmed the order.")
    return redirect('/')


@login_required
@is_delivery
def paidOrder(request):
    cart_id = request.GET.get('cart_id')

    order = Order.objects.get(cart__cart_id = cart_id)
    order.status = "Paid"
    order.save()

    return redirect("/")


@login_required
@is_delivery
def newDeliveryOrder(request):
    data = Order.objects.filter(status="Recieved", cart__is_active = True)
    if request.GET.get('per_page'):
        per_page = request.GET.get('per_page')
    else:
        per_page = 10
    paginator = Paginator(data, per_page)

    page = request.GET.get('page')
    try:
        newOrders = paginator.page(page)
    except PageNotAnInteger:
        newOrders = paginator.page(1)
    except EmptyPage:
        newOrders = paginator.page(paginator.num_pages)

    context = {
        'datas': newOrders,
        'per_page': per_page,
    }
    return render(request, "delivery/newDeliveryOrder.html", context)


@login_required
@is_delivery
def preparedDeliveryOrder(request):
    data = Order.objects.filter(status="Prepared", cart__is_active = False)
    if request.GET.get('per_page'):
        per_page = request.GET.get('per_page')
    else:
        per_page = 10
    paginator = Paginator(data, per_page)

    page = request.GET.get('page')
    try:
        preparedOrders = paginator.page(page)
    except PageNotAnInteger:
        preparedOrders = paginator.page(1)
    except EmptyPage:
        preparedOrders = paginator.page(paginator.num_pages)

    content = {
        'datas': preparedOrders,
        'per_page': per_page,
    }
    return render(request, "delivery/newDeliveryOrder.html", content)


@login_required
@is_delivery
def paidOrderList(request):
    data = Order.objects.filter(status="Paid", cart__is_active = False)
    if request.GET.get('per_page'):
        per_page = request.GET.get('per_page')
    else:
        per_page = 10
    paginator = Paginator(data, per_page)

    page = request.GET.get('page')
    try:
        preparedOrders = paginator.page(page)
    except PageNotAnInteger:
        preparedOrders = paginator.page(1)
    except EmptyPage:
        preparedOrders = paginator.page(paginator.num_pages)

    content = {
        'datas': preparedOrders,
        'per_page': per_page,
    }
    return render(request, "delivery/paidList.html", content)


@login_required
@is_delivery
def checkDeliveryNotification(request):
    newOrder = Order.objects.filter(status="Recieved", cart__is_active = True).count()
    preparedOrder = Order.objects.filter(status="Prepared", cart__is_active = False).count()

    dict = {
        "new": newOrder,
        "prepared": preparedOrder,
    }

    # jsonData = json.dumps(dict)

    return JsonResponse(dict)
