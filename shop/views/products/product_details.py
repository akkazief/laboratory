from django.views.generic import DetailView

from shop.models.product import Product

class ProductDetailView(DetailView):
    template_name = "catalog/products/detail.html"
    model = Product
    context_object_name = "product"