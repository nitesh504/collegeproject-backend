# Generated by Django 4.2.17 on 2025-01-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_venuebooking_name_alter_venuebooking_banquet"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("product", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(max_length=15)),
                ("additional_instructions", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
