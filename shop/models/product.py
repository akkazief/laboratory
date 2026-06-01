from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименовние")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey("shop.Category", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(verbose_name="Стоимость")
    img = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.name

    class Meta:
        db_table = "Товары"
        verbose_name = "Товары"
