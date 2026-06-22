from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View

from shop.models import Cart
from shop.models.product import Product

class AddToCartView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.stock < 1:
            return redirect(request.META.get("HTTP_REFERER", "main"))

        cart_item, created = Cart.objects.get_or_create(product=product)

        if not created:
            if cart_item.amount + 1 <= product.stock:
                cart_item.amount += 1
                cart_item.save()

        return redirect(request.META.get("HTTP_REFERER", "main"))
