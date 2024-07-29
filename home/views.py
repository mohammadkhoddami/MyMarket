from django.shortcuts import render
from django.views import View, generic

class HomeView(generic.TemplateView):
    template_name = 'home/index.html'