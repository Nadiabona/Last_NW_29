import pytest
from rest_framework import status

from tests.factories import AdsFactory


@pytest.mark.django_db
def test_selection_create(client, user_access_token):
    user, access_token = user_access_token
    ads_list = AdsFactory.create_batch(5)
    data = {
        "name": "my_selection",
        "items" :[ads.pk for ads in ads_list]
    }

    expected_data = {
        "id": 1, #тестовая база всегда пустая
        "owner": user.username,
        "name": "my_selection",
        "items" :[ads.pk for ads in ads_list]

    }

    response = client.post("/selection/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")
    assert response.status_code==status.HTTP_201_CREATED
    assert response.data == expected_data