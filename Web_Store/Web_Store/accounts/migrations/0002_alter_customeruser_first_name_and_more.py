# Generated by Django 4.2.4 on 2023-08-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
