# Generated by Django 5.0 on 2023-12-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fashionapp", "0005_alter_productdetails_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cart_userid", models.IntegerField()),
                ("car_producrt", models.IntegerField()),
            ],
        ),
    ]
