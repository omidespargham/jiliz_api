import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from advert.serializers import HomeCategorySerializer,GetAdvertSerialiser,CitySerializer,CategorySerializer
from advert.models import (
    Category,
    City,
    Advert
)
from django.core.cache import cache

class HomePageSearchView(APIView):
    def get(self, request):
        load_all_cities = City.objects.all()
        load_all_categories = Category.objects.filter(parent__isnull=True)
        cities = CitySerializer(instance=load_all_cities,many=True).data
        categories = CategorySerializer(instance=load_all_categories,many=True).data

        return Response({'cities': cities, 'categories': categories})



# this is for 4 adverts with category view
class HomePageDataView(APIView):
    def get(self, request):
        categorys = Category.objects.filter(parent__isnull=True)
        category_srz = HomeCategorySerializer(instance=categorys,many=True, context={'host': request.META['HTTP_HOST']})
        return Response(data=category_srz.data)


# return adverts with category 5
class HomePageCategoryDataView(APIView):
    def get(self, request, num_post, category_id):
        visble = 5
        upper = num_post
        lower = upper - visble
        get_category = Category.objects.get(id=category_id)
        load_adverts = Advert.objects.filter(categorys=get_category).order_by('-created_obj')[:upper]
        adverts_srz = GetAdvertSerialiser(load_adverts,many=True).data
        return Response(adverts_srz)


class SaveDataInCacheView(APIView):
    def post(self,request,key,value):
        # for key,value in request.data:
        cache.set(key,value)

        return Response(data={"OK":"make it as avatar !"})

class GetDataFromCacheView(APIView):
    def get(self,request,key):
        result = cache.get(key,"null")
        return Response(data={result:"you got the data !"})