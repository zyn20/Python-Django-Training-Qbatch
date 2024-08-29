# Generated by Django 4.2.15 on 2024-08-27 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0013_membership_person_group_idx_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jeep",
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
                ("name", models.CharField(max_length=20)),
                ("model", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
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
                ("reg_num", models.CharField(max_length=30)),
                (
                    "reg_type",
                    models.CharField(
                        choices=[("N", "Normal"), ("U", "Urgent")], max_length=1
                    ),
                ),
                (
                    "car",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="students.jeep"
                    ),
                ),
            ],
        ),
    ]
