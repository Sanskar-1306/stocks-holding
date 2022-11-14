import imp
from django.contrib import admin

from stocks_api import models

admin.site.register(models.Stock)
admin.site.register(models.TransactionModel)
# Register your models here.
