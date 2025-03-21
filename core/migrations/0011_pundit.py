# Generated by Django 4.2.17 on 2025-01-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_order_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pundit",
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
                ("name", models.CharField(max_length=200)),
                ("education", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image_url", models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
