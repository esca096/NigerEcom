from django.contrib import admin
from .models import Product
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('name','description', 'price', 'actif','date_time')
    
admin.site.register(Product, AdminProduct)
