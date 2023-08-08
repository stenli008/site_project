from django.core.exceptions import ValidationError
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    product_picture = models.ImageField(upload_to='product_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.category.name} - {self.name}'



