from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import product



class productListView(ListView):
    template_name = 'index.html'
    queryset = product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos '

        print(context)

        return context

class ProducDetailview(DetailView): #id
    model = product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print(context)

        return context