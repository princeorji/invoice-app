from django.contrib import admin
from .models import *

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'uuid')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'rate', 'due_date')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Service, ServiceAdmin)
