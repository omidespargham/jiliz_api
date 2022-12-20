from rest_framework import serializers
from . import models


class ShowAdvertSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    city = serializers.CharField(source='city.name_city')
    brand = serializers.CharField(source='brand.name')
    country = serializers.CharField(source='country.name')

    class Meta:
        model = models.Advert
        # fields = ('category', 'title', 'description', 'price', 'agreement_price', 'phone_number', 'slug', 'brand', 'country')
        # fields = '__all__'
        exclude = ('id', 'user')


class MakeAdvertSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    city = serializers.CharField(source='city.name_city', required=False)
    brand = serializers.CharField(source='brand.name', required=False)
    country = serializers.CharField(source='country.name', required=False)

    class Meta:
        model = models.Advert
        fields = '__all__'

    # def perform_create(self, serz):
    #
    #     serz.save(user=self.request.user, category='121', city='asa', )
    #
    # def create(self, validated_data):
    #     return models.Advert.objects.create(**validated_data)
class HomePageSearchSerializer(serializers.Serializer):
    pass

