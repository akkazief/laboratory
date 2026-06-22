from django.contrib import admin

from .models import Category, Product, Cart, Order, OrderProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "category",
        "stock",
        "price",
        "created_at",
        "img",
    )
    list_filter = ("category", "created_at", "stock")
    search_fields = ("name", "description")
    fields = ("name", "description", "category", "price", "stock", "img")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_filter = ("id", "name", "description")
    search_fields = ("name", "description")
    fields = ("name", "description")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone", "address", "created_at")
    search_fields = ("username", "phone", "address")
    fields = ("username", "phone", "address")


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
