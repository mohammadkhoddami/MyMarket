from django.urls import path
from . import views


app_name = 'payment'

urlpatterns = [
    path('payment_process/', views.PaymentProcessView.as_view(), name='payment_process'),
    path('payment_callback/', views.PaymentCallbackView.as_view(), name='payment_callback'),
]
