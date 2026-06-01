from django.contrib import admin

from .models import Category, Product

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'created_at', 'price', 'img')
    list_filter = ('id', 'name', 'description', 'category', 'created_at', 'price', 'img')
    search_fields = ('name', 'description', 'category', 'created_at', 'price', 'img')
    fields = ('name', 'description', 'category', 'created_at', 'price', 'img')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    fields = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, TaskAdmin)
admin.site.register(Category)

