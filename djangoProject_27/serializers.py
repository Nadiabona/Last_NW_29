from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import User, Location


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserListSerializer(ModelSerializer):
    total_ads = IntegerField()

    #вариант старый - хуже
    #total_ads = SerializerMethodField()

    #def get_total_ads(self, user): #обязательно, чтобы функция содержала get, нижнее подчеркивание, название поля
    #принимает объект из базы, то есть кому мы добавляем поле
        #return user.ads_set.filter(is_published = True).count()
    #ads_set - это обратное обращение к моделям

    class Meta:
        model = User
        fields = ['username', 'total_ads']

class UserDetailSerializer(ModelSerializer):
    location = SlugRelatedField(queryset=Location.objects.all(), slug_field = "name") #мз всех локаций выбараем соответствующую локацию и выводим name локации

    class Meta:
        model = User
        exclude = ['password']

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

