from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('author', 'body', 'status', 'stars')
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', )
     
    inlines = [
         CommentInline
     ]

@admin.register(Comment)
class DeactiveCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'body', 'status', 'stars')
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(status=False)