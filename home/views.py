from typing import Any
from django.shortcuts import render
from django.views import View, generic
from .models import Product
class HomeView(generic.ListView):
    queryset = Product
    template_name = 'home/index.html'
    context_object_name = 'products'
    paginate_by = 5