from rest_framework import serializers
from . import models
from django.shortcuts import get_object_or_404


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

    def validate(self, attrs):
        category = attrs['category'].get('name')
        brand = attrs['brand'].get("name")
        country = attrs['country'].get('name')
        city = attrs['city'].get('name_city')
        get_object_or_404(models.Category, name=category)
        get_object_or_404(models.Brand, name=brand)
        get_object_or_404(models.Country, name=country)
        get_object_or_404(models.City, name_city=city)
        category_in = models.Category.objects.get(name=str(category))
        city_in = models.City.objects.get(name_city=str(city))
        brand_in = models.Brand.objects.get(name=str(brand))
        country_in = models.Country.objects.get(name=str(country))

        attrs['category'] = category_in
        attrs['city'] = city_in
        attrs['brand'] = brand_in
        attrs['country'] = country_in

        return attrs



    def create(self, validated_data):
        return models.Advert.objects.create(**validated_data)


class HomePageSearchSerializer(serializers.Serializer):
    pass



    # def perform_create(self, serz):
    #     serz.save(user=self.request.user, category=serz['category'], city='asa', )