from django.urls import path
from shop.views.product_views import products_view, product_add_view, product_view, product_delete_view, product_update_view, products_by_category
from shop.views.category_views import category_add_view

urlpatterns = [
    path('', products_view, name='main'),
    path('products/', products_view, name='products'),

    path('products/add/', product_add_view, name='add_product'),
    path('categories/add/', category_add_view, name='add_category'),

    path('products/delete/<int:pk>/', product_delete_view, name='product_delete'),

    path('products/update/<int:pk>/', product_update_view, name='product_update'),

    path('products/<int:pk>/', product_view, name='product_view'),

    path('category/<str:category_name>/', products_by_category, name='products_by_category')
]