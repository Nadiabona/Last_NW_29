from rest_framework.serializers import ModelSerializer

from ads.models import Ads


class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"

