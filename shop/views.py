from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from .cart import Cart
from .forms import AddToCartProdcutForm
from home.models import Product
from django.http import HttpResponseNotAllowed, HttpResponse

class CartView(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['quantity_update_form'] = AddToCartProdcutForm(initial={
                'quantity': item['quantity'],
                'inplace': True,
            })
        return render(request, 'shop/cart.html', {'cart': cart})
        


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        response = render(request, '405.html')
        return HttpResponseNotAllowed(['POST'], response)

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = AddToCartProdcutForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            quantity = cd['quantity']
            cart.add(product=product, quantity=quantity, replace_current_quantity=cd['inplace'])
        return redirect('shop:cart')
    

class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        cart.remove(product=product)
        return redirect('shop:cart')
    
class ClearCartView(View):
    def get(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect('home:home')