import pytest
from rest_framework.test import APIClient
from auntetification.models import Product


@pytest.mark.django_db
def test_patch_product():
    p = Product.objects.create(name="Item", price=50)
    c = APIClient()
    r = c.patch(f'/api/product/{p.id}/', {"price": 75}, format='json')
    assert r.status_code == 200
    assert float(r.data["price"]) == 75
