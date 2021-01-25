# Register your models here.
from django.contrib import admin
from .models import Product  # add this


# class ProductAdmin(admin.ModelAdmin):  # add this
#     list_display = ('name', 'description', 'image')  # add this


# Register your models here.
admin.site.register(Product)  # add this
