from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ads, Category
from users.models import User


class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"

class AdsDetailSerializer(ModelSerializer):

    author_id = SlugRelatedField(slug_field = "username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field = "name", queryset=Category.objects.all())


    class Meta:
            model = Ads
            fields = "__all__"


class AdsListSerializer(ModelSerializer):
    author_id = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    address = SerializerMethodField()
    def get_address(self, ads):
        return ads.author_id.location.name

    class Meta:
        model = Ads
        fields = "__all__"




