# Generated by Django 4.2.17 on 2025-01-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_personalrecommendation_punditbooking_venuebooking"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personalrecommendation",
            name="education_paragraph",
        ),
        migrations.RemoveField(
            model_name="personalrecommendation",
            name="finance_paragraph",
        ),
        migrations.RemoveField(
            model_name="personalrecommendation",
            name="travel_paragraph",
        ),
        migrations.AddField(
            model_name="personalrecommendation",
            name="education",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="personalrecommendation",
            name="finance",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="personalrecommendation",
            name="travel",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="personalrecommendation",
            name="education_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/education/"
            ),
        ),
        migrations.AlterField(
            model_name="personalrecommendation",
            name="finance_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/finance/"),
        ),
        migrations.AlterField(
            model_name="personalrecommendation",
            name="horoscope",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="personalrecommendation",
            name="travel_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/travel/"),
        ),
    ]
