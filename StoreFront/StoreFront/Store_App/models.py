from django.db import models
from django.core.validators import MinLengthValidator


class ProductCategory(models.Model):
    COMPUTER_MOUSE = 'COMPUTER_MOUSE'
    MOUSE_PAD = 'MOUSE_PAD'
    KEYBOARD = 'KEYBOARD'
    HEADPHONES = 'HEADPHONES'
    SCREEN = 'SCREEN'
    PREBUILT_PC = 'PREBUILT_PC'
    LAPTOP = 'LAPTOP'
    CABLE = 'CABLE'
    SPEAKERS = 'SPEAKERS'
    PRINTER = 'PRINTER'
    OTHER = 'OTHER'
    CHARGER = 'Charger'

    CHOICES = (
        (COMPUTER_MOUSE, 'Computer Mouse'),
        (MOUSE_PAD, 'Mouse Pad'),
        (KEYBOARD, 'Keyboard'),
        (HEADPHONES, 'Headphones'),
        (SCREEN, 'Screen'),
        (PREBUILT_PC, 'PreBuilt PC'),
        (LAPTOP, 'Laptop'),
        (CABLE, 'Cable'),
        (SPEAKERS, 'Speakers'),
        (PRINTER, 'Printer'),
        (OTHER, 'Other'),
        (CHARGER, 'Charger'),
    )

    name = models.CharField(
        max_length=40,
        choices=CHOICES,
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

    full_name = f'{first_name} {last_name}'

    def __str__(self):
        return self.full_name


class Order(models.Model):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    DELIVERED = 'DELIVERED'

    CHOICES = (
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (DELIVERED, 'Delivered'),
    )

    status = models.CharField(
        choices=CHOICES,
        blank=False,
        null=False,
        max_length=30,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        Product,
        through='OrderItem',
    )

    order_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Order: {self.id} - Made by {Customer.full_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        blank=False,
        null=False,
    )

