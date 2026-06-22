from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View

from shop.forms import AddToCartForm
from shop.models import Cart
from shop.models import Product


class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = AddToCartForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data["amount"]

            if product.stock < 1:
                return redirect(request.META.get("HTTP_REFERER", "main"))

            cart_item, created = Cart.objects.get_or_create(product=product)

            if created:
                if amount <= product.stock:
                    cart_item.amount = amount
                    cart_item.save()
            else:
                new_amount = cart_item.amount + amount
                if new_amount <= product.stock:
                    cart_item.amount = new_amount
                    cart_item.save()

        return redirect(request.META.get("HTTP_REFERER", "main"))
