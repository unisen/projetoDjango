# Generated by Django 4.2.18 on 2025-01-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipes",
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
                ("name", models.CharField(default="", max_length=120)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("style", models.CharField(default="", max_length=200)),
                ("brewer", models.CharField(default="", max_length=100)),
                ("type", models.CharField(default="All Grain", max_length=20)),
                ("version", models.CharField(default="1", max_length=20)),
                (
                    "batch_size",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "boil_size",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "boil_time",
                    models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
                ),
                (
                    "efficiency",
                    models.DecimalField(decimal_places=1, default=75.0, max_digits=4),
                ),
                (
                    "ibu",
                    models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
                ),
                (
                    "abv",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
                ),
                ("notes", models.TextField(default="")),
                (
                    "carbonation",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
                ),
                (
                    "primary_age",
                    models.DecimalField(decimal_places=1, default=0, max_digits=4),
                ),
                (
                    "secondary_age",
                    models.DecimalField(decimal_places=1, default=0, max_digits=4),
                ),
                ("age", models.DecimalField(decimal_places=1, default=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name="Scanface",
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
                ("verified", models.CharField(default="", max_length=200)),
                ("distance", models.CharField(default="", max_length=100)),
                ("threshold", models.DecimalField(decimal_places=2, max_digits=3)),
                ("model", models.CharField(default="", max_length=200)),
                ("detector_backend", models.CharField(default="", max_length=100)),
                ("similarity_metric", models.CharField(default="", max_length=100)),
                ("facial_areas", models.CharField(default="", max_length=500)),
                ("time", models.CharField(default="", max_length=100)),
            ],
        ),
    ]
