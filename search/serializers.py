from rest_framework import serializers
from django.db.models import Q

STATUS_TYPE_CHOISES = (
    "نو", "کارکرده"
)


class AdvertSearchSerializer(serializers.Serializer):
    category = serializers.IntegerField(required=False)
    search = serializers.CharField(required=False, allow_blank=True)
    # description = serializers.CharField(required=True)
    city = serializers.IntegerField(required=False)
    brand = serializers.IntegerField(required=False)
    country_made_by = serializers.IntegerField(required=False)
    status_type = serializers.ChoiceField(
        required=False, choices=STATUS_TYPE_CHOISES)

    def make_Q_statments_for_model_querys(self, validated_data):
        search = validated_data.get("search", None)
        category = validated_data.get("category", None)
        city = validated_data.get("city", None)
        country_made_by = validated_data.get("country_made_by", None)
        brand = validated_data.get("brand", None)
        status_type = validated_data.get("status_type", None)

        search = Q(title__contains=search) | Q(
            description__contains=search) if search else Q(title__contains="")
        category = Q(categorys=category) if category else Q(title__contains="")
        city = Q(city=city) if city else Q(title__contains="")
        country_made_by = Q(country_made_by=country_made_by) if country_made_by else Q(
            title__contains="")
        brand = Q(brand=brand) if brand else Q(title__contains="")
        status_type = Q(status_type=status_type) if status_type else Q(
            title__contains="")

        return {"search": search, "category": category, "city": city,
                "country_made_by": country_made_by, "brand": brand,
                "status_type": status_type}
