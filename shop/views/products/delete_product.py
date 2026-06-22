from django.urls import reverse_lazy
from django.views.generic import DeleteView


from shop.models.product import Product


class ProductDeleteView(DeleteView):
    template_name = "catalog/products/delete.html"
    model = Product
    context_object_name = "product"
    success_url = reverse_lazy("main")