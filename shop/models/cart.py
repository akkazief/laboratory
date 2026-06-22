from django.db import models

from shop.models import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='product')
    amount = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return f"{self.product.name} x {self.amount} "

    class Meta:
        db_table = "cart_items"
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def item_total(self):
        return self.amount * self.product.price