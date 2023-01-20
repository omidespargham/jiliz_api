from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import UserSerialzier
from .models import User,RGScode
from random import randint

class LoginView(APIView):
    def post(self, request):
        srz_data = UserSerialzier(request.POST)
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


# Create your views here.
