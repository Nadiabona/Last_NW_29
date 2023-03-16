import pytest

from ads.serializers import AdsDetailSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_detail(client, access_token):
    ads = AdsFactory.create()
    response = client.get(f"/ads/{ads.pk}/", HTTP_AUTHORIZATION = "Bearer"+access_token)
    assert response.status_code==200
    assert response.data == AdsDetailSerializer(ads).data

