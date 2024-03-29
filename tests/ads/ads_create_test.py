import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ads_create(client, user, category, access_token):
    data = {
        "author_id": user.pk,
        "category_id": category.pk,
        "name": "tableVeryGood",
        "price": 200
    }

    expected_data = {
        "id": 1, #тестовая база всегда пустая
        "is_published": False,
        "name": "tableVeryGood",
        "price": 200,
        "description": None,
        "image": None,
        "author_id": user.pk,
        "category_id": category.pk
    }

    response = client.post("/ads/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")
    assert response.status_code==status.HTTP_201_CREATED
    assert response.data == expected_data
