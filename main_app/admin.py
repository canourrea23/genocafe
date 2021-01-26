# Register your models here.
from django.contrib import admin
from .models import Product, Blog  # add this


# class ProductAdmin(admin.ModelAdmin):  # add this
#     list_display = ('name', 'description', 'image')  # add this


# Register your models here.
admin.site.register(Product)
admin.site.register(Blog)  # add this
