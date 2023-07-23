from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','brand','category','price','selling_price','is_display']
    search_fields=['name','brand_name']
    search_help_text="Enter Product-Name or Brand-name"
