from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPES = [
        ('ADMIN', 'Admin'),
        ('MKTG', 'Marketing'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='MKTG')
    phone_no = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username

class BinMaster(models.Model):
    bin_no = models.CharField(max_length=6, primary_key=True)
    bin_desc = models.CharField(max_length=40, null=False)
    bin_location = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.bin_no


class ProductMaster(models.Model):
    product_id = models.CharField(max_length=6, primary_key=True)
    product_desc = models.CharField(max_length=40, null=False)
    stock_in_tons = models.DecimalField(max_digits=10, decimal_places=3)
    bin_no = models.ForeignKey(BinMaster, on_delete=models.SET_NULL, null=True, blank=True)
    product_grade = models.CharField(max_length=10)

    def __str__(self):
        return self.product_desc


class CustomerMaster(models.Model):
    customer_no = models.CharField(max_length=6, primary_key=True)
    customer_name = models.CharField(max_length=40, null=False)
    customer_address = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    phone_no = models.CharField(max_length=10)
    email_id = models.CharField(max_length=30)
    product_grade = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_name


class YardReceipts(models.Model):
    receipt_id = models.CharField(max_length=6, primary_key=True)
    transport_type = models.CharField(max_length=10, choices=[("Truck", "Truck"), ("Rail", "Rail")])
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    received_date = models.DateField()
    received_qty_in_tons = models.DecimalField(max_digits=10, decimal_places=3)
    remarks = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.receipt_id


class SaleOrder(models.Model):
    sale_order_id = models.CharField(max_length=6, primary_key=True)
    sale_order_date = models.DateField()
    customer = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    sale_order_qty_in_tons = models.DecimalField(max_digits=10, decimal_places=3)
    remarks = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.sale_order_id


class YardDespatches(models.Model):
    despatch_id = models.CharField(max_length=6, primary_key=True)
    transport_id = models.CharField(max_length=10, choices=[("Truck", "Truck"), ("Rail", "Rail")])
    despatch_date = models.DateField()
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    despatched_qty_in_tons = models.DecimalField(max_digits=10, decimal_places=3)
    remarks = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.despatch_id


