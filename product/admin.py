from django.contrib import admin

# Register your models here.
from .models import CategoryModel, BrandModel, ProductModel


admin.site.register(ProductModel)
admin.site.register(BrandModel)
admin.site.register(CategoryModel)