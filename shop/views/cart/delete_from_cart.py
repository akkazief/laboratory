from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View

from shop.models.cart import Cart


class DeleteFromCartView(View):
    def get(self, request, pk):
        cart_item = get_object_or_404(Cart, pk=pk)
        cart_item.delete()
        return redirect("cart")