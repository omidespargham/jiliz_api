from rest_framework.serializers import Serializer,ModelSerializer,StringRelatedField
from .models import student


class studentserializer(ModelSerializer):
    teacher = StringRelatedField(many=True,read_only=True)
    class Meta:
        fields = "__all__"
        model = student


