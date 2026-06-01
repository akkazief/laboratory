from django.urls import path
from shop.views import products_view, product_add_view, product_view

urlpatterns = [
    path('', products_view, name='main'),
    path('products/', products_view, name='products'),

    path('products/add/', product_add_view, name='add_product'),

    # path('products/delete_task/<int:pk>/', delete_product, name='delete_product'),

    path('products/<int:pk>/', product_view, name='product_details'),

]