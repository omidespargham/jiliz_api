from rest_framework import serializers
from . import models
from django.shortcuts import get_object_or_404
from .models import Category, Advert, City


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


# class MakeAdvertSerializer(serializers.ModelSerializer):
#     category = serializers.CharField(source='category.name')
#     city = serializers.CharField(source='city.name_city', required=False)
#     brand = serializers.CharField(source='brand.name', required=False)
#     country = serializers.CharField(source='country.name', required=False)

#     class Meta:
#         model = models.Advert
#         fields = '__all__'

#     def validate(self, attrs):
#         category = attrs['category'].get('name')
#         brand = attrs['brand'].get("name")
#         country = attrs['country'].get('name')
#         city = attrs['city'].get('name_city')
#         get_object_or_404(models.Category, name=category)
#         get_object_or_404(models.Brand, name=brand)
#         get_object_or_404(models.Country, name=country)
#         get_object_or_404(models.City, name_city=city)
#         category_in = models.Category.objects.get(name=str(category))
#         city_in = models.City.objects.get(name_city=str(city))
#         brand_in = models.Brand.objects.get(name=str(brand))
#         country_in = models.Country.objects.get(name=str(country))

#         attrs['category'] = category_in
#         attrs['city'] = city_in
#         attrs['brand'] = brand_in
#         attrs['country'] = country_in

#         return attrs

#     def create(self, validated_data):
#         return models.Advert.objects.create(**validated_data)

# this is serializer for make advert !
class MakeAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ["categorys", "title", "description", "price", "agreement_price", "address",
                  "city", "brand", "image0","image1","image2","image3","image4","image5", "status_type", "country_made_by"]
        extra_kwargs = {
                "city": {"required": True},
                "agreement_price" : {"required": True},
                # "image0" : {"required": True},
                }
    def create(self,validated_data):
        categorys_to_set = validated_data.get("categorys")
        del validated_data["categorys"]
        advert = Advert.objects.create(**validated_data)
        advert.categorys.set(categorys_to_set)
        return advert


class HomePageSearchSerializer(serializers.Serializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ("parent", "id", "name")
    # def perform_create(self, serz):
    #     serz.save(user=self.request.user, category=serz['category'], city='asa', )


class MultiSearchSerializers(serializers.Serializer):
    city = serializers.CharField(required=False)


# omid serializers
class GetAdvertSerialiser(serializers.ModelSerializer):
    image0 = serializers.SerializerMethodField()

    def get_image0(self, obj):
        if obj.image0:
            return str(self.context.get('host')) + obj.image0.url

    class Meta:
        model = Advert
        fields = ("id", "title", "description", "image0")


# this is for 4 adverts with category view
class HomeCategorySerializer(serializers.ModelSerializer):
    adverts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("parent", "id", "name", "adverts")

    def get_adverts(self, obj):
        data = self.context.get('host')
        adverts = obj.adverts.filter().order_by("-created_obj")[:10]
        adverts_srz = GetAdvertSerialiser(
            instance=adverts, many=True, context={'host': data}).data
        return adverts_srz


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name_city",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
