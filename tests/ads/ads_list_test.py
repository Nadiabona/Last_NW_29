import pytest

from ads.serializers import AdsListSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_detail(client):
    ads_list = AdsFactory.create_batch(4)

    response = client.get(f"/ads/")
    assert response.status_code==200
    assert response.data == {
        "count":4,
        "next":None,
        "previous":None,
        "results":AdsListSerializer(ads_list, many=True).data
    }
