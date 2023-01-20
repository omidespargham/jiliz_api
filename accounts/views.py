from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import UserSerialzier,UserVerifySerializer
from .models import User,RGScode
from random import randint

class LoginView(APIView):
    def post(self, request):
        srz_data = UserSerialzier(data=request.data)
        if srz_data.is_valid(): # shouldnt check the phone is unique
            the_code = randint(1, 9)
            RGScode.objects.create(
                phone_number=srz_data.validated_data["phone_number"], code=the_code)
            print(the_code)
            # if the session didnt work in DRF get the phone again in user verify view !
            request.session["user_info"] = {
                "phone_number": srz_data.validated_data["phone_number"]}
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)

class UserVerifyView(APIView):
    def post(self, request):
        srz_data = UserVerifySerializer(data=request.data)
        if srz_data.is_valid():
            # code = form.cleaned_data["code"]
            try:
                user_info = request.session["user_info"]
                user = User.objects.get(phone_number=user_info["phone_number"])

            except User.DoesNotExist:
                rand_password = User.get_random_string()
                user = User.objects.create_user(
                    phone_number=user_info["phone_number"], password=rand_password)
            
            tokens = user.get_tokens_for_user()
            return Response(data=tokens)
            
        return Response(data=srz_data.errors)

# TODO
# validations needed for loginView serialzers

