from django.urls import path, include
from rest_framework import routers

from .models import ProductModel
from .views import CategoryView, BrandView, ProductView

router = routers.DefaultRouter()
router.register(r'categories', CategoryView,basename='category')
router.register(r'brands', BrandView,basename='brand')
router.register(r'product', ProductView,basename='product')
urlpatterns = [
    path("", include(router.urls))
]