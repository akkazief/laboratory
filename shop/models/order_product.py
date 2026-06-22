from django.db import models


class OrderProduct(models.Model):
    order = models.ForeignKey(
        "shop.Order",
        on_delete=models.CASCADE,
        verbose_name="Заказ",
        related_name="order_products",
    )
    product = models.ForeignKey(
        "shop.Product",
        on_delete=models.RESTRICT,
        verbose_name="Товар",
        related_name="order_products",
    )

    amount = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.product.name} x {self.amount}"

    class Meta:
        db_table = "order_products"
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"
