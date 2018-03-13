from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.http import HttpResponse
# from django.template import loader

from django.shortcuts import render, redirect, get_object_or_404
# from requests import Response

from .models import Product
from users.decorators import is_restaurant, is_admin
from .forms import ProductCreateForm, ProductEditForm
# from django.urls import reverse
from carts.models import Cart

@login_required
@is_admin
@is_restaurant
def product_create(request):
    form = ProductCreateForm()
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("product:list")

    context = {
        "form": form
    }
    return render(request, 'products/product_edit.html', context)


@login_required()
@is_admin
@is_restaurant
def product_edit(request, pk):
    data = Product.objects.get(pk=pk)
    form = ProductEditForm(instance=data)
    if request.method == "POST":
        form = ProductEditForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("product:list")

    context = {
        "form": form
    }
    return render(request, 'products/product_edit.html', context)


# @login_required
def product_list(request):
    product_list_data = Product.objects.all().order_by('product_name')
    per_page = 8
    paginator = Paginator(product_list_data, per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if request.user.is_authenticated:
        if request.user.is_restaurant_user or request.user.is_admin:
            return render(request, 'products/product_list.html', {'products': products})

    return render(request, 'products/list.html', {'products': products})


# @login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.all().order_by('?')[:3]
    cart, new_obj = Cart.objects.new_or_get(request)
    content = {
        'product': product,
        'related': related,
        'cart': cart,
    }

    if request.user.is_authenticated:
        if request.user.is_restaurant_user or request.user.is_admin:
            return render(request, 'products/product_detail.html', content)

    return render(request, 'products/detail.html', content)

# def test(request):
#     question_id = 10
#     template = loader.get_template('base_temp.html')
#     return HttpResponse(template.render())
