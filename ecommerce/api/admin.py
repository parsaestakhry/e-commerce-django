from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Purchase)
admin.site.register(models.Product)
admin.site.register(models.Manager)
admin.site.register(models.Customer)
admin.site.register(models.Category)
admin.site.register(models.purhase_product_user)