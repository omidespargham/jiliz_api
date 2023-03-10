# from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import User, RGScode
from django.core.cache import cache

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
    # phone_number = serializers.CharField(required=True)
    code = serializers.IntegerField()

    def validate_code(self,code):
        # phone = cache.get(code,None)
        
        if len(str(code)) != 5:
            raise serializers.ValidationError("کد نامعتبر است.")
        try:
            rgs_obj = RGScode.objects.get(code=code)
            phone = rgs_obj.phone_number
            rgs_obj.delete()
        except RGScode.DoesNotExist:
            raise serializers.ValidationError("کد وجود ندارد و یا منقضی شده")
        # cache.delete_pattern(code)
        return phone
    
    # def validate_code(self,code):
    #     phone = cache.get(code,None)
    #     if len(str(code)) != 1:
    #         raise serializers.ValidationError("کد نامعتبر است.")
    #     elif not phone:
    #         raise serializers.ValidationError("کد وجود ندارد و یا منقضی شده")
    #     cache.delete_pattern(code)
    #     return phone

    
        # try:
        #     the_code = RGScode.objects.get(code=code)
        #     the_code.delete()
        #     return code
        # except RGScode.DoesNotExist:
        #     raise serializers.ValidationError("کد نامعتبر است.")
    
    
    # def validate_phone_number(self, value):
    #     if value[0:2] != "09":
    #         raise serializers.ValidationError("تلفن باید با 09 شروع شود", code="required")
    #     return value




# class UserVerifySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RGScode
#         fields = "__all__"

