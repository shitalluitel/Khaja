from django.shortcuts import render, redirect
# from .models import Address
from .forms import AddressForm
from django.urls import reverse

# Create your views here.

def address_create(request):
    if not request.session.get('cart_id') == None and not request.session.get('cart_item') == 0:
        form = AddressForm()
        if request.method == "POST":
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.user = request.user
                address.cart = request.session.get('cart_id')
                address.save()
                return redirect(reverse("cart:checkout") + '?address=%s'%(address.id))

        context = {
            "form": form
        }

        return render(request, 'address_create.html', context)

    return redirect("home")
