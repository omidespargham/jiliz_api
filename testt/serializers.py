from rest_framework.serializers import Serializer,ModelSerializer
from .models import One

class OneSerializer(ModelSerializer):
    class Meta:
        model=One
        fields = ("name","f")

