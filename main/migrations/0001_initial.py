# Generated by Django 5.1.6 on 2025-03-15 05:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BinMaster",
            fields=[
                (
                    "bin_no",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("bin_desc", models.CharField(max_length=40)),
                (
                    "bin_location",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerMaster",
            fields=[
                (
                    "customer_no",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("customer_name", models.CharField(max_length=40)),
                ("customer_address", models.CharField(max_length=40)),
                ("city", models.CharField(max_length=20)),
                ("pin", models.CharField(max_length=6)),
                ("phone_no", models.CharField(max_length=10)),
                ("email_id", models.CharField(max_length=30)),
                ("product_grade", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="ProductMaster",
            fields=[
                (
                    "product_id",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("product_desc", models.CharField(max_length=40)),
                ("stock_in_tons", models.DecimalField(decimal_places=3, max_digits=10)),
                ("product_grade", models.CharField(max_length=10)),
                (
                    "bin_no",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.binmaster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SaleOrder",
            fields=[
                (
                    "sale_order_id",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("sale_order_date", models.DateField()),
                (
                    "sale_order_qty_in_tons",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("remarks", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.customermaster",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.productmaster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "user_type",
                    models.CharField(
                        choices=[("ADMIN", "Admin"), ("MKTG", "Marketing")],
                        default="MKTG",
                        max_length=10,
                    ),
                ),
                ("phone_no", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="YardDespatches",
            fields=[
                (
                    "despatch_id",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                (
                    "transport_id",
                    models.CharField(
                        choices=[("Truck", "Truck"), ("Rail", "Rail")], max_length=10
                    ),
                ),
                ("despatch_date", models.DateField()),
                (
                    "despatched_qty_in_tons",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("remarks", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "sale_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.saleorder"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="YardReceipts",
            fields=[
                (
                    "receipt_id",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                (
                    "transport_type",
                    models.CharField(
                        choices=[("Truck", "Truck"), ("Rail", "Rail")], max_length=10
                    ),
                ),
                ("received_date", models.DateField()),
                (
                    "received_qty_in_tons",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("remarks", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.productmaster",
                    ),
                ),
            ],
        ),
    ]
