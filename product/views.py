# from django.shortcuts import render, get_object_or_404
import json
from wsgiref.util import FileWrapper
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from .models import Product
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView, View
from orders.models import Order
from stats.models import Problems

class ProductList(ListView):
    model = Product
    template_name =  'product/product_list.html'

    def get_context_data(self, **kwargs):
        stat_nos = Problems.objects.values('figure')
        stat_issue = Problems.objects.values('issue')
    
        issue_series = list()
        figure_series = list()
    
        for entry in stat_nos:
            figure_series.append(entry['figure'])
        for entry in stat_issue:
            issue_series.append(entry['issue'])
            
        context = super().get_context_data(**kwargs)
        context['issue_series'] = json.dumps(issue_series)
        context['figure_series'] = json.dumps(figure_series)
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    # queryset = list(Product.objects.values())
   
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        return context


class ProductDownloadView(LoginRequiredMixin,View):
    template_name = 'product/download.html'

    def get(self, *args, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        download_qs = Product.objects.filter(id=id, slug=slug)
        if download_qs.count() != 1:
            raise Http404("Download not found")
        download_obj = download_qs.first()
        order_qs = Order.objects.filter(user=self.request.user)
        print('The order qs', order_qs)
        if not order_qs.exists():
            messages.error(self.request, 'You MUST have a valid order to access this view.')
            return redirect('products:list')
        FILE_ROOT = settings.PROTECTED_ROOT
        filepath = download_obj.file.path
        final_filepath = FILE_ROOT / filepath
        with open(final_filepath, 'rb') as f:
            wrapper = FileWrapper(f)
            mimetype = 'application/pdf'
            response = HttpResponse(wrapper, content_type=mimetype)
            response['Content-Disposition'] = "attachment;filename="
            response['X-Sendfile'] =  str(download_obj.name)
            return response
  
