# Generated by Django 4.2.4 on 2023-08-11 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0010_alter_orderitem_order_alter_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='address',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.order'),
        ),
    ]
