from django.db import models
from django.core.validators import MinLengthValidator


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=40,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2), ],
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=300,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    phone_number = models.CharField(
        max_length=20,
    )

    address = models.CharField(
        max_length=30,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class OrderStatus(models.Model):
    status = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.status

