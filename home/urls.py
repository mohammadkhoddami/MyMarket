from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product')
]
