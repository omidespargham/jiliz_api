from rest_framework import serializers
from .models import Advert, Category
from .models import Advert, Category,Country,City,Brand
from django.utils.translation import gettext_lazy as _
# this is serializer for make advert !


class MakeAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ["categorys", "title", "description", "price", 
        # "agreement_price",
         "address","city", "brand", "image0", "image1", "image2", "image3", "image4", "image5", "status_type", "country_made_by"]
        extra_kwargs = {
            "city": {"required": True},
            # "agreement_price": {"required": True},
            "error_messages": {
                "status_type": {"invalid": _("باید نو یا کارکرده بفرستید")}
            }
            # "image0" : {"required": True},
        }

    def create(self, validated_data):
        categorys_id_to_set = validated_data.get("categorys")
        del validated_data["categorys"]
        advert = Advert.objects.create(**validated_data)
        advert.categorys.set(categorys_id_to_set)
        return advert

class AdvertDetailSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    country_made_by = serializers.StringRelatedField()
    # categorys = serializers.StringRelatedField(many=True)
    categorys = serializers.SerializerMethodField()
    class Meta:
        model=Advert
        # fields= "__all__"
        exclude = ("slug","publish","created_obj","user" )

    def get_categorys(self,obj):
        return CategorySerializer(instance=obj.categorys,many=True).data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name", "parent")

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model= Country
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields = "__all__"
