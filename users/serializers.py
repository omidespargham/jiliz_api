# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from .models import (
#     User,
#     UserCode
# )


# class UserRegisterSerializer(serializers.Serializer):
#     """ Serializers for user registration"""
#     username = serializers.CharField(write_only=True, validators=[UniqueValidator(queryset=User.objects.all())],
#                                      required=False, default=None)
#     name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#     email = serializers.EmailField(write_only=True, validators=[UniqueValidator(queryset=User.objects.all())],
#                                    required=False, default=None)
#     password1 = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)
#     phone_number = serializers.IntegerField(required=True, validators=[UniqueValidator(queryset=User.objects.all())],
#                                             write_only=True)

#     def validate(self, attrs):
#         # if self.password1 != self.password2:
#         #     raise serializers.ValidationError("Password must match")
#         if attrs['password1'] != attrs['password2']:
#             raise serializers.ValidationError('password must match')


#         elif len(str(attrs['phone_number'])) != 11:
#             raise serializers.ValidationError('Phone is not valid')

#         else:
#             return attrs


# class VerifyCodeSerializer(serializers.Serializer):
#     phone_number = serializers.IntegerField()
#     code = serializers.IntegerField()

#     def validate(self, attrs):
#         print(len(str(attrs['phone_number'])))
#         if len(str(attrs['phone_number'])) + 1 != 11:
#             raise serializers.ValidationError('Phone is not valid')

#         else:
#             return attrs