# Generated by Django 4.2.15 on 2024-08-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_order_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
