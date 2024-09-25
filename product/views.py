from sys import modules

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

from .models import CategoryModel, BrandModel, ProductModel
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryView(viewsets.ViewSet):
    """
     A viewset for viewing and editing user instances.
     """

    def list(self, request):
        queryset = CategoryModel.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        logger.info(f"Categories: {queryset}")
        return Response(serializer.data)

class BrandView(viewsets.ViewSet):

    def list(self, request):
        queryset = BrandModel.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductView(viewsets.ViewSet):

    def list(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


