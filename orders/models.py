from django.db import models
from django.conf import settings
from .validators import validate_phone_number

class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    paid = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60, verbose_name=('نام'))
    authority = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=60, verbose_name=('نام خانوادگی'))
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number], verbose_name=('شماره موبایل'))
    address = models.CharField(max_length=700, verbose_name=('آدرس'))
    order_notes = models.CharField(max_length=140, blank=True, null=True, verbose_name=('یادداشت سفارش'))
    ref_id = models.CharField(max_length=255, blank=True)
    pay_data = models.TextField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} orderd and paid: {self.paid}'
    
    class Meta:
        verbose_name_plural = "Orders"
        
    def get_total_price(self):
        total_price = sum(item.quantity *item.price for item in self.items.all())
        return total_price * 10 #Because in Iran we pay in rial currency
    
class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    products = models.ForeignKey('home.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return f'order:{self.order} - prodcuts: {self.products} - quantity: {self.quantity} - price: {self.price}'
    