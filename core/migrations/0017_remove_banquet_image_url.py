# Generated by Django 4.2.17 on 2025-01-03 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_remove_pundit_image_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="banquet",
            name="image_url",
        ),
    ]
