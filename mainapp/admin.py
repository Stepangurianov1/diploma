from django.contrib import admin

# Register your models here.
from mainapp.models import Product, Product_for_diller


# admin.site.register(Product)

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    fields = ('name', 'description', ('price'))
    ordering = ('name', 'price',)
    search_fields = ('name',)


@admin.register(Product_for_diller)
class Product_diller(admin.ModelAdmin):
    list_display = ('name', 'color', 'model', 'memory_size', 'quantity')
    fields = ('name', 'color', 'model', 'memory_size', 'quantity')
