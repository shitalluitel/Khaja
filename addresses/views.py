from django.shortcuts import render, redirect
# from .models import Address
from .forms import AddressForm
from django.urls import reverse
from carts.models import Cart
# Create your views here.

# this method is used to control the process of adding address for a cart during checkout process
def address_create(request):
    if not request.session.get('cart_id') == None and not request.session.get('cart_item') == 0:
        form = AddressForm()
        if request.method == "POST":
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.user = request.user
                address.cart = Cart.objects.get(id = request.session.get('cart_id'))
                address.save()
                return redirect(reverse("cart:checkout") + '?address=%s'%(address.id))

        context = {
            "form": form
        }

        return render(request, 'address_create.html', context)

    return redirect("home")
