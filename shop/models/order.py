from django.db import models


class Order(models.Model):
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
    phone = models.CharField(max_length=30, verbose_name="Номер телефона")
    address = models.CharField(max_length=150, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    products = models.ManyToManyField(
        "shop.Product",
        through="OrderProduct",
        verbose_name="Товары",
        related_name="orders",
    )

    def __str__(self):
        return f"№: {self.pk}"

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
