from django.views.generic import ListView

from shop.models import Cart

from shop.forms import OrderForm


class CartView(ListView):
    template_name = "catalog/cart/cart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return Cart.objects.all().select_related("product")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.get_queryset()
        context["cart_total"] = sum(item.product.price * item.amount for item in cart_items)
        context["order_form"] = OrderForm()
        return context
