from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('shop/<int:product_id>/', views.AddToCartView.as_view(), name='cart_add')
]
