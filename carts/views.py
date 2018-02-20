from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart, Quantity
from orders.models import Order


# from users.decorators import is_admin, is_customer, is_restaurant, is_delivery


# Create your views here.


def cart_home(request):
    # cart, new_obj = Cart.objects.new_or_get(request)
    cart_id = request.session.get('cart_id')
    try:
        cart = Cart.objects.get(id=cart_id, is_active=True, user=request.user)
    except:
        cart = None
    quantity = Quantity.objects.all().filter(cart=cart)
    context = {
        'cart': cart,
        'quantity': quantity,
    }
    request.session["cart_item"] = quantity.count()
    return render(request, "display_cart.html", context=context)


@login_required
def cart_update(request):
    product_id = request.GET.get('product')
    product_quantity = request.GET.get('quantity')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            # print(product_obj)
        except Product.DoesNotExist:
            return redirect("product:list")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            object = Quantity.objects.filter(cart=cart_obj, product=product_obj)
            object.delete()
        else:
            # cart_obj.products.add(product_obj)
            # cart_obj.Quantity.product = product_obj
            Quantity.objects.create(quantity=product_quantity, cart=cart_obj, product=product_obj)

        request.session["cart_item"] = cart_obj.products.count()
    return redirect("cart:display")


@login_required
def checkout_home(request):
    cart, new_obj = Cart.objects.new_or_get(request)
    order_obj = None
    if new_obj or cart.products.count() == 0:
        return redirect("cart:display")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart)
        request.session["cart_item"] = 0
        request.session['cart_id'] = None
    return render(request, "checkout.html", {"order": order_obj})
