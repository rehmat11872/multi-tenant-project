from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenant')