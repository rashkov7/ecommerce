from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

from .models import CategoryModel
from .serializers import CategorySerializer

class CategoryView(viewsets.ViewSet):
    """
     A viewset for viewing and editing user instances.
     """

    def list(self, request):
        queryset = CategoryModel.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        logger.info(f"Categories: {queryset}")
        return Response(serializer.data)



