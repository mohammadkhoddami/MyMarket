from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    picture = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home:product", kwargs={"pk": self.pk})
    