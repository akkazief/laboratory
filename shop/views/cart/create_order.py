from shop.forms import OrderForm
from shop.models import Order
from shop.models.order_product import OrderProduct
from django.views.generic import CreateView
from django.shortcuts import redirect

from shop.models.cart import Cart


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        cart_items = Cart.objects.all()

        if not cart_items.exists():
            return redirect("cart")

        order = form.save()

        cart_items = Cart.objects.all()
        for item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=item.product,
                amount=item.amount,
            )
        cart_items.delete()

        return redirect("main")