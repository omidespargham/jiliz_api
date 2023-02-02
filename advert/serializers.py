from rest_framework import serializers
from .models import Advert, Category,Country

# this is serializer for make advert !


class MakeAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ["categorys", "title", "description", "price", "agreement_price", "address",
                  "city", "brand", "image0", "image1", "image2", "image3", "image4", "image5", "status_type", "country_made_by"]
        extra_kwargs = {
            "city": {"required": True},
            "agreement_price": {"required": True},
            # "image0" : {"required": True},
        }

    def create(self, validated_data):
        categorys_id_to_set = validated_data.get("categorys")
        del validated_data["categorys"]
        advert = Advert.objects.create(**validated_data)
        advert.categorys.set(categorys_id_to_set)
        return advert


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name", "parent")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model= Country
        fields = "__all__"

