# Generated by Django 4.2.4 on 2023-08-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customeruser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='first_name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='last_name',
            field=models.CharField(),
        ),
    ]
