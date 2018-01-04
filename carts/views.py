from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart, Quantity
# from users.decorators import is_admin, is_customer, is_restaurant, is_delivery


# Create your views here.


def cart_home(request):
    cart, new_obj = Cart.objects.new_or_get(request)
    quantity = Quantity.objects.all().filter(cart=cart)
    context = {
        'cart': cart,
        'quantity': quantity,
    }
    request.session["cart_item"] = cart.products.count()
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
