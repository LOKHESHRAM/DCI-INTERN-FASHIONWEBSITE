# Generated by Django 5.0 on 2023-12-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0007_rename_car_producrt_usercart_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
