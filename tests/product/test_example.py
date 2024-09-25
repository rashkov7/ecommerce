from django.test import TestCase
from product.models import BrandModel
import pytest
from rest_framework.test import RequestsClient


pytestmark = pytest.mark.django_db


class TestBrandModel(TestCase):

    ENDPOINT = 'http://127.0.0.1:8000/product/brands/'

    def setUp(self):
        BrandModel.objects.create(brand_name="TestModel")

    def test_str_method(self):
        brand = BrandModel.objects.get(brand_name="TestModel")
        self.assertEqual(brand.__str__(), "TestModel")

    def test_endpoint(self):
        client = RequestsClient()
        response = client.get(self.ENDPOINT)
        assert response.status_code == 200

