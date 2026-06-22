from django.urls import reverse_lazy

from django.views.generic import UpdateView

from shop.models.product import Product

from shop.forms.product_form import ProductForm


class ProductUpdateView(UpdateView):
    template_name = "catalog/products/update.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("main")
