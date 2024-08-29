# Generated by Django 4.2.15 on 2024-08-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0010_cat_dog"),
    ]

    operations = [
        migrations.CreateModel(
            name="Toppings",
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
                ("t_flavour", models.CharField(max_length=50)),
                ("t_ingredient", models.CharField(max_length=20)),
                ("t_price", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
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
                ("flavour", models.CharField(max_length=50)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("S", "Small"),
                            ("M", "Medium"),
                            ("L", "Large"),
                            ("XL", "Extra Large"),
                        ],
                        default="S",
                        max_length=2,
                    ),
                ),
                ("price", models.BigIntegerField()),
                ("toppings", models.ManyToManyField(to="students.toppings")),
            ],
        ),
    ]
