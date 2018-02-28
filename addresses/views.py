from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm


# Create your views here.

def address_create(request):
    address_get = Address.objects.get(user=request.user)
    if not address_get:
        form = AddressForm()
        if request.method == "POST":
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.user = request.user
                address.save()
                return redirect("cart:checkout")

        context = {
            "form": form
        }

        return render(request, 'address_create.html', context)
    else:
        form = AddressForm(instance=address_get)
        if request.method == "POST":
            form = AddressForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("cart:checkout")
        context={
            "form": form,
        }
        return render(request, 'address_create.html', context)
    
    return redirect("cart:checkout")
