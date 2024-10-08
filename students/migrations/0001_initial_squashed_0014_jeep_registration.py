# Generated by Django 4.2.15 on 2024-08-27 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("students", "0001_initial"),
        ("students", "0002_manufacturer_car"),
        ("students", "0003_author_tailor_employee_clothes_book"),
        ("students", "0004_order_product"),
        ("students", "0005_alter_order_updated_at_alter_product_updated_at"),
        ("students", "0006_rename_name_product_p_name_and_more"),
        ("students", "0007_person_pablo"),
        ("students", "0008_delete_pablo_delete_person"),
        ("students", "0009_animal"),
        ("students", "0010_cat_dog"),
        ("students", "0011_toppings_pizza"),
        ("students", "0012_group_person_membership_group_members"),
        ("students", "0013_membership_person_group_idx_and_more"),
        ("students", "0014_jeep_registration"),
    ]

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("stu_first_name", models.CharField(max_length=50)),
                ("stu_last_name", models.CharField(max_length=50)),
                ("stu_city", models.CharField(max_length=50)),
                ("stu_email", models.EmailField(max_length=254)),
                ("stu_dob", models.DateField()),
                (
                    "stu_gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("NS", "Not Specified"),
                        ],
                        default="M",
                        max_length=2,
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
                "ordering": ["stu_last_name", "stu_first_name"],
            },
        ),
        migrations.CreateModel(
            name="Manufacturer",
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
                ("m_name", models.CharField(max_length=50)),
                ("m_is_registered", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Car",
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
                ("c_name", models.CharField(max_length=50)),
                ("c_model", models.CharField(max_length=20)),
                (
                    "menu_fact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cars",
                        to="students.manufacturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=100)),
                ("birthdate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Tailor",
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
                ("name", models.CharField(max_length=30)),
                ("location", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                (
                    "manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subordinates",
                        to="students.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Clothes",
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
                ("type", models.CharField(max_length=20)),
                (
                    "tailor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clothes",
                        to="students.tailor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="students.author",
                    ),
                ),
            ],
        ),
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="active", max_length=20)),
                ("order_number", models.CharField(max_length=50)),
                ("customer_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="active", max_length=20)),
                ("p_name", models.CharField(max_length=100)),
                ("p_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Animal",
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
            ],
        ),
        migrations.CreateModel(
            name="Cat",
            fields=[
                (
                    "animal_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="students.animal",
                    ),
                ),
            ],
            bases=("students.animal",),
        ),
        migrations.CreateModel(
            name="Dog",
            fields=[
                (
                    "animal_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="students.animal",
                    ),
                ),
            ],
            bases=("students.animal",),
        ),
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
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
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
                ("date_joined", models.DateField()),
                ("invite_reason", models.CharField(max_length=64)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="students.group"
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.person",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(
                through="students.Membership", to="students.person"
            ),
        ),
        migrations.AddIndex(
            model_name="membership",
            index=models.Index(fields=["person", "group"], name="person-group-idx"),
        ),
        migrations.AddIndex(
            model_name="membership",
            index=models.Index(fields=["-date_joined"], name="date_joined_idx"),
        ),
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
