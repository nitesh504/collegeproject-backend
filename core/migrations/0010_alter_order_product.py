# Generated by Django 4.2.17 on 2025-01-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="product",
            field=models.CharField(
                choices=[
                    ("Product 1", "Product 1"),
                    ("Product 2", "Product 2"),
                    ("Product 3", "Product 3"),
                ],
                max_length=255,
            ),
        ),
    ]
