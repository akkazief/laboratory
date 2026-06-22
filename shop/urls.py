from django.urls import path
from shop.views.products import (
    ProductsView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, ProductsByCategoryView
)
from shop.views.cart import (
    CartView, AddToCartView,
    DeleteFromCartView, DeleteOneItemView, CreateOrderView)




from shop.views.category_views import category_add_view

urlpatterns = [
    path("", ProductsView.as_view(), name="main"),
    path("products/", ProductsView.as_view(), name="products"),

    path("products/add/", ProductCreateView.as_view(), name="add_product"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_view"),
    path("products/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),

    path("categories/add/", category_add_view, name="add_category"),
    path("category/<str:category_name>/", ProductsByCategoryView.as_view(), name="products_by_category"),

    path("cart/", CartView.as_view(), name="cart"),
    path("cart/add/<int:pk>/", AddToCartView.as_view(), name="add_to_cart"),
    path("cart/remove/<int:pk>/", DeleteFromCartView.as_view(), name="delete_from_cart"),
    path("cart/remove-one/<int:pk>/", DeleteOneItemView.as_view(), name="delete_one_item"),
    path("orders/create/", CreateOrderView.as_view(), name="create_order"),
    ]