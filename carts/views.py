from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart


# Create your views here.


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return redirect("product:list")


def cart_update(request):
    product_id = request.POST.get('product')
    # quantity = request.POST.get('quantity')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            print(product_obj)
        except Product.DoesNotExist:
            return redirect("product:list")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect("product:list")
