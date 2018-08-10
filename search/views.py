# from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
import json
from django.shortcuts import HttpResponse

# from django.core.paginator import Paginator
# from django.core.paginator import EmptyPage
# from django.core.paginator import PageNotAnInteger

class SearchProductView(ListView):
    template_name = "search/view.html"
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Product.objects.filter(product_name__icontains=query)
        return Product.objects.all()


def search_option(request):
    if request.is_ajax():
        q = request.GET.get('term')
        datas = Product.objects.filter(product_name__icontains = q).order_by('?')[:5]
        result = []
        for data in  datas:
            r_data = {}
            r_data['data'] = "%s, %s" % (data.product_name, data.company.company_name)
            r_data['value'] = data.product_name
            result.append(r_data)
        json_data = json.dumps(result)
    else:
        json_data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(json_data, mimetype)
