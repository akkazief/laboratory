from django.views.generic import ListView

from shop.models.product import Product
from shop.models.category import Category
from shop.forms.product_form import ProductForm
from shop.forms.search_form import SearchForm


class ProductsView(ListView):
    template_name = "catalog/products/list_all.html"
    context_object_name = "products"

    def dispatch(self, request, *args, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_value = None
        if self.form.is_valid():
            self.search_value = self.form.cleaned_data.get("query")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.filter(stock__gte=1).order_by("category", "name")
        if self.search_value:
            queryset = queryset.filter(name__icontains=self.search_value)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.form
        context["categories"] = Category.objects.all().order_by("name")
        context["create_form"] = ProductForm()
        return context