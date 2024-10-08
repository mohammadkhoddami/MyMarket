from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from . import managers
from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveBigIntegerField()
    picture = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home:product", kwargs={"pk": self.pk})
    
    
class Comment(models.Model):
    STARS_CHOICE = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    stars = models.CharField(max_length=15, choices=STARS_CHOICE)
    
    status = models.BooleanField(default=False)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    
    # Managers
    objects = models.Manager()
    active_comment_manager =  managers.ActiveCommentManager()
    
    
    def get_absolute_url(self):
        return reverse("home:product", kwargs={"pk": self.pk})
    