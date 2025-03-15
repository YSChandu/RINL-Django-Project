from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BinMaster)
admin.site.register(ProductMaster)
admin.site.register(CustomerMaster)
admin.site.register(YardReceipts)
admin.site.register(SaleOrder)
admin.site.register(YardDespatches)
