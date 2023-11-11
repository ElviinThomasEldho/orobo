from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Quotation)
admin.site.register(Transaction)
admin.site.register(Inventory)
admin.site.register(DeliveryTracker)