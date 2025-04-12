import pytest
from rest_framework.test import APIClient
from auntetification.models import Product

@pytest.mark.django_db
def test_put_product():
    p = Product.objects.create(name="Old", price=100)
    c = APIClient()
    r = c.put(f'/api/product/{p.id}/', {"name": "New", "price": 200}, format='json')
    assert r.status_code == 200
    assert r.data["name"] == "New"
    assert float(r.data["price"]) == 200

