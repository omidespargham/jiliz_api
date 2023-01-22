# from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import User, RGScode


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number",)

    def validate_phone_number(self, value):
        if value[0:2] != "09":
            raise serializers.ValidationError([serializers.ValidationError(
                "شماره تلفن نامعتبر است", code="invalid"), serializers.ValidationError("تلفن باید با 09 شروع شود", code="required")])
        try:
            code = RGScode.objects.get(phone_number=value)
            code.delete()
        except RGScode.DoesNotExist:
            pass
        return value
    


class UserVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    code = serializers.IntegerField()

# class UserVerifySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RGScode
#         fields = "__all__"
        
