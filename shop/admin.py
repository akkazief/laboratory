from django.contrib import admin

from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'created_at', 'price', 'img', 'stock')
    list_filter = ('category', 'created_at', 'stock')
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'category', 'price', 'img', 'stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

