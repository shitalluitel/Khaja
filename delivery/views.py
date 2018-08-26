from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.decorators import is_delivery
from orders.models import Order
from carts.models import Cart, Quantity
from addresses.models import Address
# Create your views here.



@login_required
@is_delivery
def deliveryDashboard(request):
    return render(request, 'delivery/dashboard.html')


@login_required
@is_delivery
def getNewOrder(request):
    orderData = Order.objects.filter(status="Processing").order_by('-created_at')[:5]

    return render(request, 'delivery/deliveryTable.html', {'order': orderData})


@login_required
@is_delivery
def getOrderPrepared(request):
    orderData = Order.objects.filter(status="Prepared").order_by('-created_at')[:5]
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
def confirmOrder(request):
    cart_id = request.GET.get("cart_id")

    cart = Cart.objects.get(cart_id = cart_id)

    order_id = request.GET.get('order_id')
    order = Order.objects.get(order_id = order_id)

    order.status = "Processing"
    order.save()

    cart.is_active = False
    cart.save()
    # return HttpResponse("Comfirmed the order.")
    return redirect('/')


@login_required
@is_delivery
def changeDeliveryStatus(request):
    pass
