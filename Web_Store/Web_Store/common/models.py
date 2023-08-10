import uuid

from django.core.exceptions import ValidationError
from django.db import models

from Web_Store.accounts.models import CustomerUser


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

    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    complete = models.BooleanField(default=False, blank=True, null=True)
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
        return f'Order: {self.transaction_id} made by {self.customer.username}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f'Item: {self.product.name} in {self.order.__str__()}'


class Shipping(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order} - {self.address}'
