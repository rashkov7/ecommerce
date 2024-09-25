from django.urls import path, include
from rest_framework import routers

from .models import ProductModel
from .views import CategoryView, BrandView

router = routers.DefaultRouter()
router.register(r'categories', CategoryView,basename='category')
router.register(r'brands', BrandView,basename='brand')
urlpatterns = [
    path("", include(router.urls))
]