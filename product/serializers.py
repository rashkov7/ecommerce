from rest_framework import serializers

from .models import BrandModel, CategoryModel, ProductModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = ProductModel
        fields = "__all__"