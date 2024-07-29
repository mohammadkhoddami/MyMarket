from typing import Any
from django.shortcuts import render
from django.views import View, generic
from .models import Product
class HomeView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'home/index.html'
    context_object_name = 'products'
    paginate_by = 5
    
class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'home/product-details.html'
    context_object_name = 'product'