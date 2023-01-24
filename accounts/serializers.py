# from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import User, RGScode


# class UserSerialzier(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("phone_number",)
class UserSerialzier(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate_phone_number(self, value):
        if value[0:2] != "09":
            raise serializers.ValidationError("تلفن باید با 09 شروع شود", code="required")
        
            # raise serializers.ValidationError([serializers.ValidationError(
            #     "شماره تلفن نامعتبر است", code="invalid"), serializers.ValidationError("تلفن باید با 09 شروع شود", code="required")])
        try:
            code = RGScode.objects.get(phone_number=value)
            code.delete()
        except RGScode.DoesNotExist:
            pass
        return value
    


class UserVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    code = serializers.IntegerField()

    def validate_code(self,code):
        try:
            the_code = RGScode.objects.get(code=code)
            the_code.delete()
            return code
        except RGScode.DoesNotExist:
            raise serializers.ValidationError("کد نامعتبر است.")
# class UserVerifySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RGScode
#         fields = "__all__"

