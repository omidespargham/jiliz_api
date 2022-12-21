from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import (
    User,
    UserCode,

)
from rest_framework import status
from random import randint as rn
from rest_framework.permissions import IsAuthenticated


class Index(APIView):
    def get(self):
        return HttpResponse("Dreams for ever")


class RegisterApiView(APIView):
    """ Custom api view for user register """

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data, write_only=True)
        print('in the post method ')
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data['username'],
                                            name=serializer.validated_data['name'],
                                            last_name=serializer.validated_data['last_name'],
                                            email=serializer.validated_data['email'],
                                            phone_number=serializer.validated_data['phone_number'])
            user.is_active = False
            user.save()
            UserCode.objects.create(phone_number=serializer.validated_data['phone_number'], code=rn(1000, 9999))
            return Response({'success': 'OTP code send sucsessfuly'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeApiView(APIView):

    @staticmethod
    def check_user(phone_number):
        try:
            user = User.objects.get(phone_verify=phone_number)
            if user.is_active == True or user.phone_verify == True:
                return Response({'error': 'phone_number is already verified'}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({'error': 'There is no user with this phone phone_number'})

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                return self.check_user(phone_number=serializer.validated_data['phone_number'])

            except:
                pass

            try:
                UserCode.objects.get(phone_number=serializer.validated_data['phone_number'])

            except UserCode.DoesNotExist:
                return Response({'error': 'There is no otp code with this phone number'},
                                status=status.HTTP_404_NOT_FOUND)

            try:
                user_code = UserCode.objects.get(phone_number=serializer.validated_data['phone_number'],
                                                 code=serializer.validated_data['code'])
                user_code.delete()
                get_user = User.objects.get(phone_number=serializer.validated_data['phone_number'])
                get_user.is_active = True
                get_user.phone_verify = True
                get_user.save()
                return Response({'success': 'phone verified successfully '}, status=status.HTTP_200_OK)

            except UserCode.DoesNotExist:
                return Response({'error': 'code is wrong'})

            # return Response({'sucsess': 'dreams for ever'})

        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResendCodeForRegisterApiView(APIView):

    @staticmethod
    def resend_code(phone_number):
        try:
            check_user = User.objects.get(phone_number=phone_number)
            if check_user.is_active == True or check_user.phone_number == True:
                return Response({'error': 'Phone is already verified '})

        except:
            pass

        try:
            get_user_code = UserCode.objects.get(phone_number=phone_number)
            print(get_user_code)
            # return Response({'error': 'Code is already exits'}, {
            #     'time to resend_code': {'minute': get_user_code.expired_time.minute,
            #                             'second': get_user_code.expired_time.second}})

            return Response({'error': 'code is already exits'})



        except UserCode.DoesNotExist:
            UserCode.objects.create(phone_number=phone_number, code=rn(1000, 9999))
            return Response({'success': 'Code has been sent'})

    @staticmethod
    def check_user(self, phone_number):
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.is_active == True or user.phone_verify == True:
                return Response({'error': 'phone_number is already verified'}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({'error': 'There is no user with this phone phone_number'},
                            status=status.HTTP_400_BAD_REQUEST)

        return self.resend_code(phone_number=phone_number)

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)

        if serializer.is_valid():

            # return self.resend_code(phone_number=serializer.validated_data['phone_number'])
            return self.check_user(self, phone_number=serializer.validated_data['phone_number'])


        else:
            return Response({
                'error': serializer.errors
            })

# class TestAuth(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         return Response({'success': 'you are login already'})
#
