from django.shortcuts import render, HttpResponse
from carts.models import Quantity
from django.contrib.auth.decorators import login_required
from users.decorators import is_restaurant
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import timedelta
from django.utils import timezone
from products.models import Product
import json
from .models  import Company
from .forms import CompanyForm
from dateutil.relativedelta import relativedelta


status_list = ["New","Received","Preparing","Cooked","Delivered","Canceled"]

# this method is used to edit the company details
@login_required
@is_restaurant
def company_edit(request):
    data = Company.objects.get(company_id = request.user.company.company_id)
    form = CompanyForm(instance=data)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=data)
        if form.is_valid():
            company = form.save()
            return redirect("home")

    context = {
        "form": form
    }
    return render(request, 'company/company_profile.html', context)


# this method helps to count number of new order_list
# it response with html page which is managed by jquery in frontend
@login_required
@is_restaurant
def check_notification(request):
    company = request.user.company
    try:
        count = Quantity.objects.filter(cart__is_active= False, product__company = company, status="New").count()
        request.session['order_no'] = count
        return render(request, 'company/notification.html',{'count': count})
    except Quantity.DoesNotExist:
        return render(request, 'company/notification.html',{'count': count})


# this method is used to query all the prodects associated with a company
# after querying it returns html page as a result with list of associated product of a company
def company_product_list(request):
    company_id = request.GET.get("company")
    company_name = Company.objects.get(company_id= company_id)
    try:
        product_list_data = Product.objects.filter(company= company_name)
    except Product.DoesNotExist:
        return redirect("product:list")

    per_page = 8
    paginator = Paginator(product_list_data, per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'company/company_product_list.html', {'products': products, 'company':company_name})


# this method is used to list orderd products with all type of status
@login_required
@is_restaurant
def order_new_list(request):
    request.session['order_no'] = Quantity.objects.filter(
                                            cart__is_active= False,
                                            product__company = request.user.company,
                                            status="New").count()
    status = request.GET.get("status")
    if status not in status_list:
        status= "New"
    products, per_page = order_list_query(request=request, status=status)
    return render(request, 'company/order_list.html', {'datas': products, 'per_page': per_page, 'status': status })


# this method accept status of order and return products object and number of items per pages
@login_required
@is_restaurant
def order_list_query(request, status):
    company = request.user.company
    try:
        data = Quantity.objects.filter(cart__is_active= False, product__company = company, status =status ).order_by("-timestamp")
    except Quantity.DoesNotExist:
        return render(request, 'company/notification.html', {'count': 0})

    if request.GET.get('per_page'):
        per_page = request.GET.get('per_page')
    else:
        per_page = 10
    paginator = Paginator(data, per_page)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return products, per_page


# this method is used to redirect towards restaurant user dashboard
@login_required
@is_restaurant
def chart(request):
    request.session['order_no'] = Quantity.objects.filter(cart__is_active= False, product__company = request.user.company, status="New").count()
    return render(request, 'dashboard.html')


# this method is used to find total amount of transaction on a day
# it gives HttpResponse
@login_required
@is_restaurant
def get_day_total(request):
    day_total = Quantity.objects.filter(
        timestamp__gte = (timezone.now() - timedelta(hours=20)),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
    )
    total = 0
    for data in day_total:
        total += data.product.product_price * data.quantity
    return HttpResponse("<strong><i class=\"fa fa-money \"></i> &nbsp; %s </strong> "%(total))


# this method is used to find total amount of transaction on a month
# it gives HttpResponse
@login_required
@is_restaurant
def get_month_total(request):
    month_total = Quantity.objects.filter(
        timestamp__gte = (timezone.now() - timedelta(weeks=4)),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
    )
    total = 0
    for data in month_total:
        total += data.product.product_price * data.quantity
    return HttpResponse("<strong><i class=\"fa fa-money \"></i> &nbsp; %s </strong> "%(total))


# this method is used to find total amount of transaction on a year
# it gives HttpResponse
@login_required
@is_restaurant
def get_year_total(request):
    year_total = Quantity.objects.filter(
        timestamp__gte = (timezone.now() + relativedelta(years=-1)),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
    )
    total = 0
    for data in year_total:
        total += data.product.product_price * data.quantity
    return HttpResponse("<strong><i class=\"fa fa-money \"></i> &nbsp; %s </strong> "%(total))


# this methos returns number of total product for a restaurant
@login_required
@is_restaurant
def total_product(request):
    return HttpResponse("<strong> %s</strong>" % (Product.objects.filter(company = request.user.company).count()))


# this method is used to retrub json response containing hourly money transaction for a day
# to display on a chart on a dash board
@login_required
@is_restaurant
def get_day_data(request):
    start_time = (timezone.now() - timedelta(hours=24))
    end_time = timezone.now()
    datas = Quantity.objects.filter(
        timestamp__range = (start_time, end_time),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
        )

    labels = []
    return_data = [] # data that gets returned

    for i in range(0,24):
        total = 0
        new_data = datas.filter(timestamp__range =(start_time + timedelta(hours = i), start_time + timedelta(hours=(i+1)) ))
        for data in new_data:
            total += data.product.product_price * data.quantity
        if total > 0:
            return_data.append(str(total))
            labels.append("%s"%((timezone.now() - timedelta(hours = 24 -i)).strftime("%I %p")))

    response_data = {}
    response_data['labels'] = labels
    response_data['data'] = return_data
    response_data['label'] = "Transaction within a day"
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# this method is used to retrub json response containing weekly money transaction for a month
# to display on a chart on a dash board
@login_required
@is_restaurant
def get_month_data(request):
    start_time = (timezone.now() - timedelta(weeks=4))
    end_time = timezone.now()
    datas = Quantity.objects.filter(
        timestamp__range = (start_time, end_time),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
        )

    labels = []
    return_data = [] # data that gets returned
    for i in range(0,4):
        total = 0
        temp_str = ""
        new_data = datas.filter(timestamp__range =(start_time + timedelta(weeks = i), start_time + timedelta(weeks=(i+1)) ))
        for data in new_data:
            total += data.product.product_price * data.quantity
        if total > 0:
            return_data.append(str(total))
            if i + 1 == 1:
                temp_str += "1st"
            elif i + 1 == 2:
                temp_str += "2nd"
            elif i + 1 == 3:
                temp_str += "3rd"
            else:
                temp_str += "4th"
            labels.append(temp_str + " week")

    response_data = {}
    response_data['labels'] = labels
    response_data['data'] = return_data
    response_data['label'] = "Transaction within a month"
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# this method is used to retrub json response containing monthly money transaction for a year
# to display on a chart on a dash board
@login_required
@is_restaurant
def get_yearly_data(request):
    start_time = (timezone.now() + relativedelta(months=-12)) + relativedelta(days= -int(timezone.now().strftime('%d'))+1)
    end_time = timezone.now()
    datas = Quantity.objects.filter(
        timestamp__range = (start_time, end_time),
        cart__is_active = False,
        product__company = request.user.company,
        status='Delivered'
        )

    labels = []
    return_data = [] # data that gets returned
    count = 0
    for i in range(0,12):
        total = 0
        new_data = datas.filter(timestamp__range =(start_time + relativedelta(months = i), start_time + relativedelta(months=(i+1)) ))
        count = count + 1
        end_time = start_time + relativedelta(months= (i+1))
        print("%s.  %s    ,,,,,,    %s" % (count,(start_time + relativedelta(months = i)).strftime('%B %d'), (start_time + relativedelta(months=(i+1))).strftime('%B %d') ))
        print(new_data)
        for data in new_data:
            total += data.product.product_price * data.quantity
        if total > 0:
            return_data.append(str(total))
            labels.append("%s"%((timezone.now() - relativedelta(months = 12 -i)).strftime("%B")))

    new_data = datas.filter(timestamp__range = (end_time, timezone.now()))
    print("%s.  %s    ,,,,,,    %s" % (count + 1,end_time.strftime('%B %d'), timezone.now().strftime('%B %d') ))
    print(new_data)
    total = 0
    for data in new_data:
        total += data.product.product_price * data.quantity
    if total > 0:
        return_data.append(str(total))
        labels.append("%s"%((timezone.now()).strftime("%B")))

    response_data = {}
    response_data['labels'] = labels
    response_data['data'] = return_data
    response_data['label'] = "Transaction within a month"
    return HttpResponse(json.dumps(response_data), content_type="application/json")
