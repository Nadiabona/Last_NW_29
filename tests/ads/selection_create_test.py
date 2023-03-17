# import pytest
# from rest_framework import status


# @pytest.mark.django_db
# def test_selection_create(client, user, access_token):
#     data = {
#         "author_id": user.pk,
#         "name": "tableVeryGood",
#         "price": 200
#     }
#
#     expected_data = {
#         "id": 1, #тестовая база всегда пустая
#         "is_published": False,
#         "name": "tableVeryGood",
#         "price": 200,
#         "description": None,
#         "image": None,
#         "author_id": user.pk,
#     }

    # response = client.post("/selection/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")
    # assert response.status_code==status.HTTP_201_CREATED
    # assert response.data == expected_data