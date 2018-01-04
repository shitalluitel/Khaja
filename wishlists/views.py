from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import WishList
from users.decorators import is_customer


# Create your views here.
@login_required
@is_customer
def create(request, pk):
    try:
        wishlist = WishList.objects.get(user=request.user, product_id=pk)
    except WishList.DoesNotExist:
        wishlist = WishList.objects.create(user=request.user, product_id=pk)
        wishlist.save()
        return redirect("wishlist:list")

    wishlist.delete()
    request.session["wishlist_item"] = WishList.objects.filter(user=request.user).count()
    return redirect("wishlist:list")


def list(request):
    wishlist_list_data = WishList.objects.all()
    per_page = 12
    paginator = Paginator(wishlist_list_data, per_page)
    page = request.GET.get('page')

    try:
        wishlists = paginator.page(page)
    except PageNotAnInteger:
        wishlists = paginator.page(1)
    except EmptyPage:
        wishlists = paginator.page(paginator.num_pages)

    request.session["wishlist_item"] = WishList.objects.filter(user=request.user).count()
    return render(request, 'wishlists/list.html', {'wishlists': wishlists})
