from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    description = models.TextField(
        max_length=500, null=True, blank=True, verbose_name="Описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
