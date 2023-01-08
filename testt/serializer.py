from rest_framework.serializers import Serializer,ModelSerializer
from .models import student


class studentserializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = student


