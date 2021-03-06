from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse, reverse
from products.models import Product
from .models import Cart, Quantity
from orders.models import Order
from addresses.models import Address
from users.decorators import is_restaurant
from company.views import order_list_query
# from users.decorators import is_admin, is_customer, is_restaurant, is_delivery


# Create your views here.

# this method  is usd to get all the info about
# the cart for an user and redirect it with that
# info to html page
@login_required
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

# this method is used to add item to cart and delete item from a cart
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


# this is used to render the order list page for a user after successful checkout process
@login_required
def checkout_home(request):
    cart, new_obj = Cart.objects.new_or_get(request)
    address = Address.objects.get(id=request.GET.get("address"))
    if not address:
        return redirect("address:create")
    else:
        order_obj = None
        if new_obj or cart.products.count() == 0:
            return redirect("cart:display")
        else:
            order_obj, new_order_obj = Order.objects.get_or_create(address=address, user=request.user, cart=cart)
            # cart.is_active = False
            # cart.save()
            request.session["cart_item"] = 0
            request.session["cart_id"] = None
        return render(request, "checkout.html", {"order": order_obj})


# this method is used to destroy cart
@login_required
def cart_destroy(request, pk):
    try:
        cart = Cart.objects.get(user=request.user, id=pk)
    except Cart.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        cart.delete()
        request.session['cart_item'] = 0
        request.session['cart_id'] = None
        # messages.success(request, "Transaction %s deleted." % (item.title))
        return redirect('home')

    context = {
        'next': reverse('/')
    }
    return render(request, 'delete.html', context)


# this method is used to change the status of the item whic are ordered
@login_required
@is_restaurant
def change_status(request):
    check = ['New','Received', 'Preparing', 'Cooked', 'Delivered']
    id = request.GET.get('id')
    value = request.GET.get('value')
    if value in check:
        try:
            quantity = Quantity.objects.get(id=id)
            quantity.status = value
            quantity.save()
            if value == 'Delivered':
                order = Order.objects.get(cart__id = quantity.cart_id)
                order.status = "Prepared"
                order.save()
            # request.session['order_no'] = Quantity.objects.filter(cart__is_active= False, product__company = request.user.company, status="New").count()
            status = request.GET.get('next')
            products, per_page = order_list_query(request=request, status=status)
            return render(request, 'order_list_table.html', {'datas': products, 'per_page': per_page})
        except Quantity.DoesNotExist:
            return HttpResponse("Unable to change the state of reservation.")
