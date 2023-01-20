# from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import User,RGScode

class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ("phone_number",)
        

# class UserVerifySerializer(serializers.Serializer):
#     phone_number = serializers.CharField(required=True)
#     code = serializers.IntegerField()

class UserVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = RGScode
        fields = "__all__"
        
