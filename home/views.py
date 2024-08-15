from typing import Any
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Product, Comment
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'home/index.html'
    context_object_name = 'products'
    paginate_by = 5
    
class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'home/product-details.html'
    context_object_name = 'product'
    # Can use created comment manager here but i prefer to not to use it 
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
        

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'home/product-details.html'
    
    def get_success_url(self):
        return reverse('home:product', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pk = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=pk)
        obj.product = product
        messages.success(self.request, 'Your comment added successfully', 'success')
        return super().form_valid(form)