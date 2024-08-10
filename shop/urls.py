from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart')
]
