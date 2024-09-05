from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from orders.models import Orders
import requests
import json
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse

class PaymentProcessView(View):
    def post(self, request):
        order_id = request.session['order_id']
        order = get_object_or_404(Orders, pk=order_id)
        total_price = order.get_total_price()
        url = 'https://api.zarinpal.com/pg/v4/payment/request.json'
        
        request_headers = {
            'accept' : 'application/json',
            'content-type' : 'application/json'
        }
        request_parameters = {
            'metchan_id': settings.MERCHANT_ID,
            'amount': total_price,
            'description': f"""
            OrderNotes: {order.id}, {order.order_notes},
            Customer_name: {order.first_name}, {order.last_name},
            address: {order.address}
            """,
            'callback_url':request.build_absolute_url(reverse('payment:payment_callback')),
            
        }   
        
        response = requests.post(url, data=json.dumps(request_parameters), headers=request_headers)
        authority = response.json()['data']['authority']
        order.authority = authority
        order.save()
        if 'errors' not in response.json()['data'] or len(response.json()['errors']) == 0:
            return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
        else: 
            return HttpResponse('There is some errors!')

class PaymentCallbackView(View):
    def get(self, request):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        order = get_object_or_404(Orders, authority=authority)
        total_price = order.get_total_price()
        if status == 'OK':
            request_headers = {
                'accept': 'application/json',
                'content-type': 'application/json',
            }
            request_parameters = {
                'merchant_id': settings.MERCHANT_ID,
                'amount': total_price,
                'authority': authority,
            }
            url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'
            response = requests.post(url, data=json.dumps(request_parameters), headers=request_headers)
            data = response.json()['data']
            
            if 'data' in response.json() and ('errors' not in data or len(data['errors'])) == 0:
                response_code = data['code']
                if response_code == 100:
                    order.paid = True
                    order.ref_id = data['ref_id']
                    order.pay_data = data
                    order.save()
                    return HttpResponse ('You payment was successful')
                
                elif response_code == 101:
                    return HttpResponse ('You payment was succesful but we haved checekd it')
                else:
                    return HttpResponse ('Your payment was unseccessful')
        return HttpResponse ('Your payment was unseccessful')