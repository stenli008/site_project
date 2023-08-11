import uuid

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from Web_Store.accounts.models import CustomerUser


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    product_picture = models.ImageField(upload_to='product_pics/', blank=False, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.category.name} - {self.name}'


class Order(models.Model):
    CHOICES = [
        ('CANCELED', 'Canceled'),
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('SENT', 'Sent'),
        ('DELIVERED', 'Delivered'),
    ]

    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=30, choices=CHOICES, default='PENDING')

    @property
    def get_order_total(self):
        order_items = self.orderitem_set.all()
        order_total = sum([item.get_total for item in order_items])
        return order_total

    @property
    def get_order_items(self):
        order_items = self.orderitem_set.all()
        order_total = sum([item.quantity for item in order_items])
        return order_total

    @property
    def get_address(self):
        try:
            shipping = Shipping.objects.get(order=self)
            address = f'{shipping.address}, {shipping.city}'
            return address
        except Shipping.DoesNotExist:
            return None

    def __str__(self):
        return f'Order: {self.transaction_id}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f'Item: {self.product.name} in {self.order.__str__()}'


class Shipping(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order} - {self.address}'
