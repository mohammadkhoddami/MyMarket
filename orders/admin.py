from django.contrib import admin
from .models import OrderItems, Orders

class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    fields = ['order', 'products', 'quantity', 'price']
    extra = 1
    
    
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'paid')
    
    inlines = [
        OrderItemsInline
    ]