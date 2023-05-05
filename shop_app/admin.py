from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Brand)



class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'quant', 'price']
    list_filter=("brand","size","gender")
    search_fields = ("title","brand")

admin.site.register(Products,ProductsAdmin)



class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'brand', 'quant', 'price']
    list_filter=("brand","size")
    search_fields = ("user","title","brand")

admin.site.register(Cart, CartAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'brand', 'quant', 'price']
    list_filter=("brand","size")
    search_fields = ("user","title","brand")

admin.site.register(Order, OrderAdmin)



admin.site.register(Favorite)