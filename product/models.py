from email.policy import default

from django.db import models

# Create your models here.
class BrandModel(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name='Brand Name')

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.brand_name


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Category Name')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class ProductModel(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Product Name')
    description = models.CharField(max_length=255, verbose_name='Descriptions')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    in_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name