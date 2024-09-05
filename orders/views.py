from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from django.contrib import messages
from shop.cart import Cart
from .models import OrderItems
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class CheckoutView(View):
    form_class = OrderForm
    temp = 'orders/checkout.html'
    
    
    def setup(self, request, *args, **kwargs):
        self.cart = Cart(request)
        return super().setup(request, *args, **kwargs)
        
    def dispatch(self, request, *args, **kwargs):
        if len(self.cart) == 0:
            messages.error(request, 'Please select a product to checkout', 'warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        form = self.form_class()
        return render(request, self.temp, {'form': form})
    
    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            for item in self.cart:
                products = item['product_obj']
                OrderItems.objects.create(order=form_obj,
                                          products=products,
                                          quantity=item['quantity'],
                                          price=products.price)
            self.cart.clear()
            
            if not request.user.first_name and not request.user.last_name:
                request.user.first_name = form_obj.first_name
                request.user.last_name = form_obj.last_name
                request.user.save()
            
            request.session['order_id'] = form_obj.id
            messages.success(request,'Your order has been added', 'success')
            return redirect('payment:payment_process')
        return render(request, self.temp, {'form': form})
    
