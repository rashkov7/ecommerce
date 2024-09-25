from email.policy import default

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class BrandModel(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name="Brand Name")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.brand_name


class CategoryModel(MPTTModel):
    category_name = models.CharField(max_length=255, verbose_name="Category Name")
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["category_name"]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class ProductModel(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.CharField(max_length=255, verbose_name="Descriptions")
    in_sale = models.BooleanField(default=False)

    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "CategoryModel", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
