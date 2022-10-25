from django.contrib import admin

from applications.models import MyProductsModel, ApplicationModel


@admin.register(MyProductsModel)
class Product_diller(admin.ModelAdmin):
    list_display = ('user_name', 'name_application', 'model', 'quantity')
    fields = ('user_name', 'name_application', 'model', 'quantity')


@admin.register(ApplicationModel)
class Application_diller(admin.ModelAdmin):
    list_display = ('name', 'user_name', 'city', 'description', 'is_active')
    fields = ('name', 'user_name', 'city', 'description', 'is_active')
