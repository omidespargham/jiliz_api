from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerialzier(ModelSerializer):
    class Meta:
        model= User
        fields = ("phone_number",)
        



