
from rest_framework import serializers
from advert.models import Category,Advert


# this is for 4 adverts with category view
class HomeCategorySerializer(serializers.ModelSerializer):
    adverts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("parent", "id", "name", "adverts")

    def get_adverts(self, obj):
        data = self.context.get('host')
        adverts = obj.adverts.filter().order_by("-created_obj")[:10]
        adverts_srz = HomeGetAdvertSerialiser(
            instance=adverts, many=True, context={'host': data}).data
        return adverts_srz

#  this can be one serialzier with advert MakeAdvertSerializer 
class HomeGetAdvertSerialiser(serializers.ModelSerializer):
    image0 = serializers.SerializerMethodField()

    def get_image0(self, obj):
        if obj.image0:
            return str(self.context.get('host')) + obj.image0.url

    class Meta:
        model = Advert
        fields = ("id", "title", "description", "image0")
