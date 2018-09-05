from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from users.decorators import is_restaurant, is_admin
from .forms import ProductCreateForm, ProductEditForm
from company.models import Company
from carts.models import Cart, Quantity
from company.views import chart
from delivery.views import deliveryDashboard
from django.contrib import messages
# from .tasks import *c


#for creating product list  and adding item to menu
@login_required
@is_restaurant
# @is_admin
def product_create(request):
    form = ProductCreateForm()
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.company = request.user.company
            product.save()
            messages.success(request, "Product " + product.product_name + " Created Successfully.")
            return redirect("product:create")

    context = {
        "form": form
    }
    return render(request, 'products/product_edit.html', context)


#to edit menu
@login_required()
# @is_admin
@is_restaurant
def product_edit(request, pk):
    data = Product.objects.get(pk=pk)
    form = ProductEditForm(instance=data)
    if request.method == "POST":
        form = ProductEditForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            product = form.save(commit=False)
            product.company = request.user.company
            product.save()
            return redirect("product:list")

    context = {
        "form": form
    }
    return render(request, 'products/product_edit.html', context)


#display all items in menu
# @login_required
def product_list(request):
    # display.delay()
    try:
        if request.user.is_authenticated:
            if request.user.user_type == 1:
                product_list_data = Product.objects.all()
                companies = Company.objects.all()
            else:
                product_list_data = Product.objects.filter(company=request.user.company)
        else:
            companies = Company.objects.all()
            product_list_data = Product.objects.all().order_by('product_name')
    except Product.DoesNotExist:
        return redirect("product:create")

    if request.user.is_authenticated:
        if request.user.user_type == 1:
            per_page = 8
        else:
            per_page = 10
    else:
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
        if request.user.user_type == 2 or request.user.is_admin:
            request.session["order_no"] = Quantity.objects.filter(cart__is_active= False, product__company = request.user.company, status='New').count()
            return render(request, 'products/product_list.html', {'products': products})

    return render(request, 'products/list.html', {'products': products, 'companies':companies})

#delete item form menu
@login_required
@is_restaurant
def product_delete(request, pk):
    item = Product.objects.get(company=request.user.company, id=pk)
    if request.method == 'POST':
        try:
            Product.objects.deleteItem(company=request.user.company, id=pk)  # item is a database
        except Product.DoesNotExist:
            raise Http404()
        return redirect('product:list')

    context = {
        'item': item
    }
    return render(request, 'delete.html', context)

#detail information about item in a menu
# @login_required
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    related = Product.objects.all().order_by('?')[:3]
    cart, new_obj = Cart.objects.new_or_get(request)
    content = {
        'product': product,
        'related': related,
        'cart': cart,
    }

    if request.user.is_authenticated:
        if request.user.user_type == 2 or request.user.is_admin:
            return render(request, 'products/product_detail.html', content)

    return render(request, 'products/detail.html', content)

@login_required
@is_restaurant
def product_inactive_list(request):
        try:
            if request.user.is_admin:
                product_list_data = Product.objects.inactive()
            else:
                product_list_data = Product.objects.inactive(company__id=request.user.company.id)
        except Product.DoesNotExist:
            return redirect("product:create")

        per_page = 10

        paginator = Paginator(product_list_data, per_page)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)


        request.session["order_no"] = Quantity.objects.filter(cart__is_active= False, product__company = request.user.company, status='New').count()
        return render(request, 'products/product_list.html', {'products': products})


@login_required
@is_restaurant
def product_restore(request, pk):
    try:
        product = Product.objects.restore(company_id = request.user.company.id, id=pk)
    except Product.DoesNotExist:
        Http404()

    return redirect("product:inactive")

#used for redirecting the login user to resperictive pages

def homeURL(request):
    if request.user.is_authenticated:
        if request.user.user_type == 1:
            return product_list(request=request)
        elif request.user.user_type == 2:
            return chart(request=request)
        elif request.user.user_type == 3:
            return deliveryDashboard(request= request)
    else:
        # return redirect('product:list')
        return product_list(request=request)
