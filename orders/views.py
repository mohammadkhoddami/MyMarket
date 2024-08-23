from django.shortcuts import render
from django.views import View
from .forms import OrderForm


class CheckoutView(View):
    form_class = OrderForm
    temp = 'orders/checkout.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.temp, {'form': form})
