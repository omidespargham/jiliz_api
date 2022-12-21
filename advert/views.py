import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Advert,
    Category,
    Brand,
    Country


)
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import (
    ShowAdvertSerializer,
    MakeAdvertSerializer

)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ShowAdvertApiView(APIView):
    def get(self, request, slug):
        get_object_or_404(Advert, slug=slug)
        obj = Advert.objects.get(slug=slug)
        serializer = ShowAdvertSerializer(instance=obj)
        return Response({'obj': serializer.data})


class MakeAdverb(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MakeAdvertSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save(category=serializer.validated_data['category'], city=serializer.validated_data['city'], brand=serializer.validated_data['brand'], country=serializer.validated_data['country'])
            return Response({'ok', 'Dreams for ever'})


        return Response({'error': serializer.errors})


