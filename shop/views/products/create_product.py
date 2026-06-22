from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.forms.product_form import ProductForm

class ProductCreateView(CreateView):
    template_name = "catalog/products/create.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy("product_view", kwargs={"pk": self.object.pk})