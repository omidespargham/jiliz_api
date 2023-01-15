from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import InstallRepairMakeSerializer
from rest_framework.response import Response


class InstallRepairMakeView(APIView):
    def post(self, request):
        serialized = InstallRepairMakeSerializer(data=request.data)
        if serialized.is_valid():
            return Response(data={"its": "ok"})
        return Response(data=serialized.errors)


# Create your views here.
