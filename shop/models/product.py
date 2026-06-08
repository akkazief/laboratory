from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименовние")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey("shop.Category", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(verbose_name="Стоимость", max_digits=7, decimal_places=2)
    img = models.URLField(verbose_name="Ссылка на изображение")
    stock = models.PositiveIntegerField(verbose_name="Остаток", default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
