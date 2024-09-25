from django.urls import path, include
from rest_framework import routers

from .models import ProductModel
from .views import CategoryView

router = routers.DefaultRouter()
router.register(r'categories', CategoryView,basename='category')
urlpatterns = [
    path("", include(router.urls))
]